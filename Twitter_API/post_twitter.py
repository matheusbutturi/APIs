import oauth2
import json
import urllib.parse

# Get the consumer and token (key/secret) params to access Twitter API
consumer_key = 'xxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxx'

token_key = 'xxxxxxxxxxxxxxxxxxx'
token_secret = 'xxxxxxxxxxxxxxxxxxxx'

# Input the objects into consumers and token to have access
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

# Gets the new tweet text to post
query = input("Novo tweet: ")

# Translate the new tweet to the url language
query_codificada = urllib.parse.quote(query, safe='')

# Makes the request POST
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada,
                             method='POST')

# Decode the post
decodificar = requisicao[1].decode()

# Transform the JSON data
objeto = json.loads(decodificar)

# Print the post
print(objeto)
