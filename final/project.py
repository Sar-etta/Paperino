import tweepy as tw
import streamlit as st
import pandas as pd
import TextBlob

st.title("try-out project")

#pip install tweepy

# import tweepy
#import tweepy as tw

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

#import pandas as pd

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


#from textblob import TextBlob
def sentiment_analysis(tweet):
 def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity
  
 #Create a function to get the polarity
 def getPolarity(text):
   return TextBlob(text).sentiment.polarity
  
 #Create two new columns ‘Subjectivity’ & ‘Polarity’
 tweet["TextBlob_Subjectivity"] =    tweet["tweet"].apply(getSubjectivity)
 tweet ["TextBlob_Polarity"] = tweet["tweet"].apply(getPolarity)
 def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'
 tweet ["TextBlob_Analysis"] = tweet  ["TextBlob_Polarity"].apply(getAnalysis )
 return tweet

for row in tweets_df["text"]:
    sentiment_analysis('tweet')
