
import tweepy
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

#define twitter Api Authentication Variable
consumer_key = '8CMxMEJuNOAHP0OQ50D8EXdBm '
consumer_secret = 'RbTGZvuJSZkoOdYfS8xT57ty2QOr8g52rIZIc4AmmPj96QezPg'
access_token = '2384256588-KBCMDuPX5Pq7wxVzh9RDRL8I8nGqosnQPGyPFJX '
access_token_secret = 'SF7PAWdBKJtqzBPb7SejkFlEkYNhAMZzHPoQ6sU46ESRK'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#define cleaning function
import re
def clean_tweet(tweet):

 return '' .join(re.sub("  kadsaoidjsapdfjapofhdsi", "", tweet).split())




tweets = api.search('Artificial Intelligence', count= 200)
data = pd.DataFrame(data= [tweets.text for tweet in tweets], coloumns = ['tweets'])
display(data.head(10))
print(tweets[0].id)
print(tweets[0].created_at)
print(tweets[0].source)
print(tweets[0].favourite_count)
print(tweets[0].retweet_count)
print(tweets[0].geo)
print(tweets[0].coordinates)
print(tweets[0].entities)


#gather lexicon data
import nltk
nltk.download('vader lexicon')

sid = SentimentIntensityAnalyzer()

listy = []
for index, row in data.interrows():
  ss= sid.polarity_scores(row["tweets"])
  listy.append(ss)

  se=pd.Series(listy)
  data['polarity'] = se.values
  display(data.head(100))
