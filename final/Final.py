import streamlit as st

urlfoto = "https://raw.githubusercontent.com/Sar-etta/Paperino/main/final/twitter_logo_banner.jpg"
st.image(urlfoto)

st.title("Sentiment Analysis through Twitter")
st.caption("The aim of this app is to analyze the sentiment of a certain topic, through an hashtag, and to give as a result a pie-chart that shows summarized the general opinion of it. To use it, just write down the topic you want analyzed, for example: #Zendaya, #covid and so on, and at the end one can decide if translating the tweets or not. #HaveFun!")

import tweepy as tw

# your Twitter API key and API secret
my_api_key = "OdbKALsXbXFIvkTtvun3lhnej"
my_api_secret = "QPjcJF2cZAtmoNira5svbAXkKWuL7Ou0FnFcWpiyRScfvL7dzl"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = st.text_input('What topic are you interest in?', "#Zendaya", help='A suggestion: insert # before typing the topic you are interested in!')   #-filter:retweets)
  
  
# get tweets from the API
tweets = tw.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              since="2020-09-16").items(50)

# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
    
st.write("In this App the total Tweets fetched is:", len(tweets_copy))

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
st.subheader('These are the overall result of the analysis:')
st.write('- The negative tweets analyzed are: ', negative)
st.write('- The neutral tweets analyzed are: ', neutral)
st.write('- The positive tweets analyzed are: ', positive)


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

translator = Translator()

#tweets_df_json = json.dumps(new_tweets_df.text.to_dict()) #new_tweets_df.text.to_json() --> sono la stessa cosa
#st.write(tweets_df_json)
#TypeError: the JSON object must be str, bytes or bytearray, not NoneType
#this is the  error, but with the lines before (*type...) on googlecollab it says it is a string, so I don't get what I should do

# Iterate over key/value pairs in dict and print them
#for key, value in tweets_df_json.items():
#    st.write(key, ' : ', value)
# --> con il codice commentato alla linea 137, se provavo a ordinarlo con questo for-loop mi diceva che non si poteva perché non dict
#MI DA SEMPRE ERROREEEEEEEEE

st.subheader("Here you can translate the Tweets fetched")
option = st.selectbox('Do you want to translate the tweets?', ('No', 'Yes'))
if option == 'Yes':
  targetl = st.text_input(" Write the two letter of the destination language: ","it", help="Write a two letter code for the language you want to translate in. For example: it, de, es, en...")
  for _, row in new_tweets_df.iterrows():
    text = row["text"]
    itrans = translator.translate (text, dest = targetl)
    st.write('the translation: ', itrans.text)
  st.info("Thank you for using this App!")
else:
  st.info("Thank you for using this App!")
  pass

#########################################

st.markdown("""---""")

st.write("Credits:")
st.write("""- How to use Tweepy and Pandas Dataframe: https://datascienceparichay.com/article/get-data-from-twitter-api-in-python-step-by-step-guide/""")
st.write("""- For the Sentiment Analysis through Textblob: https://neptune.ai/blog/sentiment-analysis-python-textblob-vs-vader-vs-flair""")
st.write("""- How to use Matplotlib: https://pythonwife.com/matplotlib-with-streamlit/""")
st.write("""- Source of the photo used: https://dustinstout.com/wp-content/uploads/2012/09/twitter-header-post.png""")
