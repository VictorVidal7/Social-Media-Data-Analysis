import tweepy

# Your keys and tokens
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Autenticación con tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creando una instancia de la API
api = tweepy.API(auth)

# Usando search_tweets para buscar tweets que contengan una palabra clave
for tweet in api.search_tweets(q="tecnología", lang="es", count=10):
    print(tweet.text)
