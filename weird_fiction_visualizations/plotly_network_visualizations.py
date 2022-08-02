import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from bokeh.io import show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8
from bokeh.transform import linear_cmap
import plotly.graph_objects as go

edges_df = pd.read_csv(r'weird_fiction_visualizations\gephi_edges.csv')
edges_df = edges_df.dropna()
edges_df['target'] = edges_df['target'].astype('int')

G = nx.from_pandas_edgelist(edges_df, 'source', 'target')

title = 'Weird Fiction Discussion Board Visualization'

HOVER_TOOLTIPS = [('Poster', '@index')]

plot = figure(tooltips=HOVER_TOOLTIPS,
    tools='pan, wheel_zoom, save, reset', active_scroll='wheel_zoom',
    x_range = Range1d(-50, 50), y_range = Range1d(-50, 50), title=title)

network_graph = from_networkx(G, nx.spring_layout, scale=50, center=(0,0))

network_graph.node_renderer.glyph = Circle(size=15, fill_color='skyblue')

network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)

plot.renderers.append(network_graph)
show(plot)

degrees = dict(nx.degree(G))
nx.set_node_attributes(G, name='degree', values=degrees)
number_to_adjust_by = 5
adjusted_node_size = dict([(node, degree+number_to_adjust_by) for node, degree in nx.degree(G)])
nx.set_node_attributes(G, name='adjusted_node_size', values=adjusted_node_size)

size_by_this_attribute = 'adjusted_node_size'
color_by_this_attribute = 'adjusted_node_size'

color_palette = Purples8

HOVER_TOOLTIPS_1 = [('Poster', '@index'), ('Degree', '@degree')]
plot = figure(tooltips=HOVER_TOOLTIPS_1,
    tools='pan, wheel_zoom, save, reset', active_scroll='wheel_zoom',
    x_range = Range1d(-50, 50), y_range = Range1d(-50, 50), title=title)

network_graph = from_networkx(G, nx.spring_layout, scale=50, center=(0,0))
minimum_value_color = min(network_graph.node_renderer.data_source.data[color_by_this_attribute])
maximum_value_color = max(network_graph.node_renderer.data_source.data[color_by_this_attribute])
network_graph.node_renderer.glyph = Circle(size=size_by_this_attribute, fill_color=linear_cmap(color_by_this_attribute, color_palette, minimum_value_color, maximum_value_color))

#Set edge opacity and width
network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)

plot.renderers.append(network_graph)

show(plot)

'''
# Trying to color-code nodes based on semester and week_read (following https://community.plotly.com/t/not-able-to-change-the-marker-color-based-on-the-column-value/46374): 
fig = go.Figure(data=go.Scattergeo(
        lon = df['long'],
        lat = df['lat'],
        text = df['text'],
        mode = 'markers',
        marker_color = df['cnt'],
        ))

fig = go.Figure(data=go.Scattergeo(
        semester = edges_df['semester'],
        week_read = edges_df['week_read'],
        mode = 'markers',
        marker_color = semester_colors,
        ))
''' 

semester_colors = np.unique(edges_df['semester'].values)
fig = go.Figure(
    data=go.Scattergeo(semester=edges_df['semester'], 
    week_read=edges_df['week_read'], 
    mode='markers', marker_color=semester_colors))

fig.update_layout(title='The Customer Locations')
fig.show()
