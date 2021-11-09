from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", encoding='utf-8')
print(df.head())

sia = SentimentIntensityAnalyzer()

negative = []
neutral = []
positive = []
compound = []

for n in range(df.shape[0]):
    title = df.iloc[n, 0]
    date = df.iloc[n, 1]
    description = df.iloc[n,2]
    analyzed_titles = sia.polarity_scores(title)
    analyzed_description = sia.polarity_scores(description)
    negative.append(((analyzed_titles['neg'])+(analyzed_description['neg']))/2)
    neutral.append(((analyzed_titles['neu'])+(analyzed_description['neu']))/2)
    positive.append(((analyzed_titles['pos'])+(analyzed_description['pos']))/2)
    compound.append(((analyzed_titles['compound'])+(analyzed_description['compound']))/2)
df["Negative"] = negative
df["Neutral"] = neutral
df["Positive"] = positive
df["Compound"] = compound

pd.set_option('display.max_columns', None)
print(df.head())
