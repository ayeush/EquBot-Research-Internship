#importing modules
import snscrape.modules.twitter as sntwitter
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
import string
import emoji
import re
from statistics import mean
import matplotlib.pyplot as plt

#creating list and appending tweets containing "interest rate" to the list
tweet_list = []
tweet_dates = []
for t, tweet in enumerate(
        sntwitter.TwitterSearchScraper('interest rate since:2021-01-01 until:2021-11-01').get_items()):
    if t > 1000:
        break
    tweet_list.append([tweet.content])
    tweet_dates.append([tweet.date])
tweets_df = pd.DataFrame(tweet_list, columns=['Tweet Content'])

#converting tweets to all lowercase
lowercase_tweet_list = []
for t in tweet_list:
    for word in t:
        lowercase_tweet_list.append(word.lower())

tokenized_tweets = [word_tokenize(tweet) for tweet in lowercase_tweet_list]

#getting rid of unnecessary punctuation
regex = re.compile('[%s]' % re.escape(string.punctuation))
tokenized_tweets_no_punctuation = []
for review in tokenized_tweets:
    tweet_list_no_punctuation = []
    for token in review:
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            tweet_list_no_punctuation.append(new_token)
    tokenized_tweets_no_punctuation.append(tweet_list_no_punctuation)

#removing stopwords
tokenized_tweets_no_stopwords = []
for no_punc_tweet in tokenized_tweets_no_punctuation:
    new_term_vector = []
    for word in no_punc_tweet:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    tokenized_tweets_no_stopwords.append(new_term_vector)

#lemmatization
wordnet = WordNetLemmatizer()
processed_tweets = []
for tokenised_tweet in tokenized_tweets_no_stopwords:
    final_tweet_list = []
    for lowercase_word in tokenised_tweet:
        final_tweet_list.append(wordnet.lemmatize(lowercase_word))
    processed_tweets.append(final_tweet_list)

final = []
for i in processed_tweets:
    listToStr = ' '.join([str(word) for word in i])
    final.append(listToStr)

sia = SentimentIntensityAnalyzer()
testrunNegative = []
testrunNeutral = []
testrunPositive = []
testrunCompound = []
for tweet in final:
    testrun = sia.polarity_scores(tweet)
    testrunNegative.append(testrun['neg'])
    testrunNeutral.append(testrun['neu'])
    testrunPositive.append(testrun['pos'])
    testrunCompound.append(testrun['compound'])

avgNeg = (sum(testrunNegative)/len(testrunNegative))
avgNeu = (sum(testrunNeutral)/len(testrunNeutral))
avgPos = (sum(testrunPositive)/len(testrunPositive))
avgCom = (sum(testrunCompound)/len(testrunCompound))
labels = ['negative', 'neutral', 'positive']
sizes = [avgNeg, avgNeu, avgPos]
plt.pie(sizes, labels=labels, autopct='%1.1f%%') # autopct='%1.1f%%' gives you percentages printed in every slice.
plt.axis('equal')  # Ensures that pie is drawn as a circle.
plt.show()

x = tweet_dates
y = testrunCompound
lineMin = [min(tweet_dates)]
lineMax = [max(tweet_dates)]
plt.plot(x, y, color='green', linestyle='dashed', linewidth=0.5, marker='.', markerfacecolor='blue', markersize=5)
plt.axhline(y=0, color='r', linestyle='-')
plt.ylim(-1, 1)
plt.xlabel('Date')
plt.ylabel('Compound Score')
plt.title('Interest Rate - Sentiment Scores Over Time')
plt.show()

posCountList = []
negCountList = []
for item in testrunCompound:
    if item > 0:
        posCountList.append(item)
    elif item < 0:
        negCountList.append(item)
    else:
        break
posCount = len(posCountList)
negCount = len(negCountList)

y_frequency = [posCount, negCount]
pos_neg = ['positive count', 'negative count']
fig = plt.figure(figsize=(10, 5))
# creating the bar plot
plt.bar(pos_neg, y_frequency, color='maroon',
        width=0.4)
plt.xlabel("Positive and Negative Tweets Count")
plt.ylabel("Frequency")
plt.title("Positive to Negative Ratio")
plt.show()