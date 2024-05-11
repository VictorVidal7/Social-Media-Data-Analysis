import tweepy

# Your keys and tokens
consumer_key = 'Pu3GdjAoClNhHHFNqgIqjLATH'
consumer_secret = 'xvNfymeHyzvUA1eElYOYLjwNvdeTWjcUqRYY9SRQbfpdekebHo'
access_token = '1768031798129295361-5TRykIlOToNTWEqH3HHZgwjIqemTZ1'
access_token_secret = 'fEfjGpR2ev9UYAmpljd9Xgmg2Mdk95uadBRV1T4SpQYCh'

# Autenticación con OAuth 2.0
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAADn4tgEAAAAALU%2FQl9iJ1Dvivl1qDvz9EsAebvg%3DNO6VlaJtgNEZHbvGxVnp3IEfLysCjCQDOccymbmrou0P2QpZ7d')

# Realizar una búsqueda utilizando la API v2
query = 'tecnología lang:es'
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(tweet.text)
