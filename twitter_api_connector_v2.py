import tweepy

# Your keys and tokens
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Autenticación con OAuth 2.0
client = tweepy.Client(bearer_token='')

# Realizar una búsqueda utilizando la API v2
query = 'tecnología lang:es'
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(tweet.text)
