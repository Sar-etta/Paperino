import streamlit as st

#from PIL import Image
#opening the image
#image = Image.open('twitter_logo_banner.jpg')
#displaying the image on streamlit app
#st.image(image, caption='Enter any caption here')


urlfoto = "https://raw.githubusercontent.com/Sar-etta/Paperino/main/final/twitter_logo_banner.jpg"
st.image(urlfoto)

st.title("Sentiment Analysis through Twitter")
st.caption("The aim of this app is to analyze the sentiment of a certain topic, through an hashtag, and to give as a result a pie-chart that shows summarized the general opinion of it.")

import tweepy as tw

# your Twitter API key and API secret
my_api_key = "OdbKALsXbXFIvkTtvun3lhnej"
my_api_secret = "QPjcJF2cZAtmoNira5svbAXkKWuL7Ou0FnFcWpiyRScfvL7dzl"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = st.text_input('What topic are you interest in?', help='insert # before typing the topic you are interested in!')   #-filter:retweets)
  
  
# get tweets from the API
tweets = tw.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              since="2020-09-16").items(50)

# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
    
st.write("Total Tweets fetched:", len(tweets_copy))

st.info('Wait a moment please, the analysis will be ready soon!')

import pandas as pd

# intialize the dataframe
tweets_df = pd.DataFrame()
  
# populate the dataframe
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name, 
                                              'user_location': tweet.user.location,\
                                              'user_description': tweet.user.description,
                                              'user_verified': tweet.user.verified,
                                              'date': tweet.created_at,
                                              'text': text, 
                                              'hashtags': [hashtags if hashtags else None],
                                              'source': tweet.source}))
    tweets_df = tweets_df.reset_index(drop=True)

# show the dataframe
#st.write(tweets_df.head())
with st.expander("If you click here, you can see the first tweets that have been collected!"):
    st.write(tweets_df.head())

#these are just the tweets of the dataframe
#st.text(tweets_df["text"])

#the dataframe with fewer columns, if later i want to append the polarity column
new_tweets_df = tweets_df.loc[ 0: ,['user_name', 'user_location', 'text']]
#st.write(new_tweets_df.head())

#in theory they are string, but i think they are just a column of the dataframe like before
tweets_in_str = new_tweets_df.text.astype(str)
#st.write(tweets_in_str)

import textblob
from textblob import TextBlob

polarity_score = []
#for-loop to analyze the sentiment
for i in range(0, new_tweets_df.shape[0]):
  score = TextBlob(tweets_df.iloc[i]["text"])
  score1 = score.sentiment[0]
  polarity_score.append(score1)
  #st.write(score1)
  

#to count the neg/neu/pos
negative = 0
neutral = 0
positive = 0

for el in polarity_score:
  if el >= -1 and el < 0:
    negative +=1
  elif el == 0:
    neutral +=1
  elif el > 0 and el <= 1:
    positive +=1
  else:
    pass

#st.write('These are the overall results of the sentiment analysis:', textColor = #5F9EA0)
st.write('these are the overall result of the analysis:')
st.write('the negative tweets analyzed are: ', negative)
st.write('the neutral tweets analyzed are: ', neutral)
st.write('the positive tweets analyzed are: ', positive)



import matplotlib.pyplot as plt
import numpy as np

y = np.array([negative, neutral, positive])
mylabels = ["negative", "neutral", "positive"]

fig = plt.figure(figsize=(10, 4))
plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

st.balloons()
st.pyplot(fig)

#############################################################################

import gtts
import googletrans
from gtts import gTTS
from googletrans import Translator

#import json,requests
#from pprint import pprint

translator = Translator()

#tweets_df_json = new_tweets_df.text.to_json()
#st.write(tweets_df_json)

option = st.selectbox('Do you want to translate the tweets?', ('Yes', 'No'))
if option == 'Yes':
  targetl = st.text_input(" write the two letter of the destination language: ", "it")
  trans= translator.translate (new_tweets_df, dest= targetl)
  st.write('the translation: ', trans.text)
else:
  pass
