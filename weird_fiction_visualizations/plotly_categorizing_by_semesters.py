import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
from bokeh.io import show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8
from bokeh.transform import linear_cmap

df = pd.read_csv(r"weird_fiction_visualizations\gephi_edges.csv")
df = df.dropna()
df['target'] = df['target'].astype('int')

G = nx.from_pandas_edgelist(df, 'source', 'target', create_using=nx.Graph())
pos = nx.drawing.layout.spring_layout(G)
nx.set_node_attributes(G, pos, 'pos')
title = 'Weird Fiction Discussion Board Visualization'

colors = list(zip(df.source, df.semester))


#print(np.unique(df['semester'].values))

'''
for node in G:
    if node in df['semester'].values == 'Fall 2019':
        colors.append('red')
    elif node in df['semester'].values == 'Fall 2020':
        colors.append('blue')
    
    elif node in df['semester'].values == 'Fall 2021':
        colors.append('yellow')
    elif node in df['semester'].values == 'Spring 2020':
        colors.append('mediumorchid')
    elif node in df['semester'].values == 'Spring 2021':
        colors.append('gold')
    elif node in df['semester'].values == 'Spring 2022':
        colors.append('magenta')
    elif node in df['semester'].values == 'Summer 2020':
        colors.append('brown')
    elif node in df['semester'].values == 'Summer 2021':
        colors.append('purple')
'''
color_dictionary = {'Fall 2019': 'red', 'Fall 2020': 'blue', 'Fall 2021': 'green', 'Spring 2020': 'mediumorchid', 'Spring 2021': 'gold', 'Spring 2022': 'magenta', 'Summer 2020': 'brown', 'Summer 2021': 'purple'}

df['color'] = df['semester'].map(color_dictionary)
print(df.head())
print(df.tail())
edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='Viridis',
        reversescale=True,
        #color=df.color,
        size=10,
        line_width=2))

for node in enumerate(G.adjacency):


fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()
