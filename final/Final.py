import streamlit as st

st.title("Final-title")

import tweepy as tw

# your Twitter API key and API secret
my_api_key = "OdbKALsXbXFIvkTtvun3lhnej"
my_api_secret = "QPjcJF2cZAtmoNira5svbAXkKWuL7Ou0FnFcWpiyRScfvL7dzl"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = st.text_input("insert a word precedeed by #: ")   #-filter:retweets)

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
st.write(tweets_df.head())

st.text(tweets_df["text"])



new_tweets_df = tweets_df.loc[ 0: ,['user_name', 'user_location', 'text']]
st.write(new_tweets_df.head())



tweets_in_str = new_tweets_df.text.astype(str)
st.write(tweets_in_str)



import TextBlob

polarity_score = []

for i in range(0, new_tweets_df.shape[0]):
  score = TextBlob(tweets_df.iloc[i]["text"])
  score1 = score.sentiment[0]
  polarity_score.append(score1)
  st.write(score1)
  
  
  
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
st.write('the negative tweets are: ', negative)
st.write('the neutral tweets are: ', neutral)
st.write('the positive tweets are: ', positive)



import matplotlib.pyplot as plt
import numpy as np

y = np.array([negative, neutral, positive])
mylabels = ["negative", "neutral", "positive"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

st.pyplot(figure)
