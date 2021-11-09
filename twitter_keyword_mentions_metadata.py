#importing modules
import snscrape.modules.twitter as sntwitter
import os
import pandas as pd
import matplotlib.pyplot as plt


# counting how many times "interest rate" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'interest rate'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterInterestRate = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterInterestRate = df.size
print('Number Of Interest Rate Tweets : ' + str(counterInterestRate))

# counting how many times "inflation rate" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'inflation rate'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterInflationRate = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterInflationRate = df.size
print('Number Of Inflation Rate Tweets : ' + str(counterInflationRate))

# counting how many times "unemployment" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'unemployment'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterUnemployment = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterUnemployment = df.size
print('Number Of Unemployment Tweets : ' + str(counterUnemployment))

# counting how many times "cryptocurrency" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'cryptocurrency'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterCryptocurrency = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterCryptocurrency = df.size
print('Number Of Cryptocurrency Tweets : ' + str(counterCryptocurrency))

# counting how many times "foreign trade" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'foreign trade'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterForiegnTrade = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterForiegnTrade = df.size
print('Number Of Foreign Trade Tweets : ' + str(counterForiegnTrade))

keywordcount = [counterInterestRate, counterInflationRate, counterUnemployment, counterCryptocurrency, counterForiegnTrade]
labels = ['interest rate', 'inflation rate', 'unemployment', 'cryptocurrency', 'foreign trade']
fig = plt.figure(figsize=(10, 5))
# creating the bar plot
plt.bar(labels, keywordcount, color='maroon',
        width=0.4)
plt.xlabel("Keyword")
plt.ylabel("Amount of mentions (10/31 to 11/1)")
plt.title("Mentions of a Keyword Metadata")
plt.show()



'''
# counting how many times "interest rate" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'interest rate'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterInterestRate = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterInterestRate = df.size
print('Number Of Tweets : ' + str(counterInterestRate))

# counting how many times "inflation rate" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'inflation rate'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterInflationRate = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterInflationRate = df.size
print('Number Of Tweets : ' + str(counterInflationRate))

# counting how many times "foreign trade" appeared in a tweet from Oct 31, 2021 to Nov 1, 2021
os.system(f"snscrape --since {'2021-10-31'} twitter-search '{'foreign trade'} until:{'2021-11-1'}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counterForiegnTrade = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counterForiegnTrade = df.size
print('Number Of Tweets : ' + str(counterForiegnTrade))

labels = ['interest rate', 'inflation rate', 'foreign trade']
keywordcount = [counterInterestRate, counterInflationRate,counterForiegnTrade]
fig = plt.figure(figsize=(10, 5))
# creating the bar plot
plt.bar(labels, keywordcount, color='maroon',
        width=0.4)
plt.xlabel("Keyword")
plt.ylabel("Amount of mentions")
plt.title("Mentions of a Keyword Metadata")
plt.show()
'''