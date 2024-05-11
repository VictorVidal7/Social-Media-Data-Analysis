import tweepy

# Your keys and tokens
consumer_key = 'Pu3GdjAoClNhHHFNqgIqjLATH'
consumer_secret = 'xvNfymeHyzvUA1eElYOYLjwNvdeTWjcUqRYY9SRQbfpdekebHo'
access_token = '1768031798129295361-5TRykIlOToNTWEqH3HHZgwjIqemTZ1'
access_token_secret = 'fEfjGpR2ev9UYAmpljd9Xgmg2Mdk95uadBRV1T4SpQYCh'

# Autenticación con tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creando una instancia de la API
api = tweepy.API(auth)

# Usando search_tweets para buscar tweets que contengan una palabra clave
for tweet in api.search_tweets(q="tecnología", lang="es", count=10):
    print(tweet.text)