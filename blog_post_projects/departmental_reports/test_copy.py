import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('test.csv')
list_of_outcomes = [1, 2, 3, 4]

def create_dummy_means(datalist):
    dummy = {}
    for item in datalist:
        dummy[item] = round(random.uniform(1, 3), 1)
    return dummy

# Much easier way than the create_dummy_means function: dictionary comprehension:
historical_mean_scores = {i: round(random.uniform(1, 3), 1) for i in range(1, len(list_of_outcomes)+1)}
print(historical_mean_scores)
#historical_mean_scores = create_dummy_means(list_of_outcomes)
print(df.groupby(['instructor', 'outcome']).mean())
print(df.groupby(['outcome', 'instructor']).agg({'score': ['mean']}))

p_df = pd.pivot_table(df, values='score', index='instructor', aggfunc='mean')
p_df.plot.bar(rot=45)
plt.xlabel("Instructor")
plt.ylabel("Mean Score")
plt.title("Mean Scores on All Outcomes by Instructor")
plt.show()

#sub_table = df.reindex(columns=[2020], level='year')

#print(toy_df.groupby('outcome').score.mean())
#print(toy_df[toy_df.instructor=='S. Snape'].score.mean())
#toy_df.groupby('instructor').score.mean().plot(kind='bar')
#plt.show()
#
#mean_scores = pd.pivot_table(toy_df, values='score', index='instructor', aggfunc='mean')
#mean_scores.plot(kind='bar')
#plt.show()

#mean_by_instructor = pd.pivot_table(toy_df, values=['score', 'outcome'], index='instructor', aggfunc='mean')
#print(mean_by_instructor)
#mean_by_instructor.plot(kind='bar')
#plt.show()

sns.barplot(x='outcome', y='score', hue='instructor', data=df, ci=None)
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
plt.show()

ax = plt.subplot()
df.groupby('outcome').score.mean().plot.bar(color=['b', 'g', 'r', 'tab:cyan'], label='_no_legend_', rot=45)
#df.groupby('outcome').score.mean().plot(kind='bar', color=['black', 'red', 'green', 'blue'], label='_no_legend_', rot=45)
plt.axhline(y=historical_mean_scores.get(1),xmin=0, xmax=1, label='1 Historical Mean', color='b', linestyle='dashed')
plt.axhline(y=historical_mean_scores.get(2),xmin=0, xmax=1, label='2 Historical Mean', color='g', linestyle='dashed')
plt.axhline(y=historical_mean_scores.get(3),xmin=0, xmax=1, label='3 Historical Mean', color='r', linestyle='dashed')
plt.axhline(y=historical_mean_scores.get(4),xmin=0, xmax=1, label='4 Historical Mean', color='tab:cyan', linestyle='dashed')
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
plt.xlabel("Outcome")
plt.ylabel("Mean Score")
plt.title("Mean Scores by Outcome")
plt.tight_layout()
plt.show()
