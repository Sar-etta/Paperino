import tweepy as tw

# your Twitter API key and API secret
my_api_key = "OdbKALsXbXFIvkTtvun3lhnej"
my_api_secret = "QPjcJF2cZAtmoNira5svbAXkKWuL7Ou0FnFcWpiyRScfvL7dzl"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = st.text_input("insert a word precedeed by #: ")   #-filter:retweets)

# get tweets from the API
tweets = tw.Cursor(api.search,
              q=search_query,
              lang="en",
              since="2020-09-16").items(50)

# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
    
st.write("Total Tweets fetched:", len(tweets_copy))
