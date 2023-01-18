import oauth2
import json
import urllib.parse

# Access parameters into Twitter
api_key = 'xxxxxxxxx'
api_key_secret = 'xxxxxxxxx'
access_token = 'xxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxx'

# Authentication using the accessing parameters
consumer = oauth2.Consumer(api_key, api_key_secret)
token = oauth2.Token(access_token, access_token_secret)
cliente = oauth2.Client(consumer, token)

# Ask the query sentence
query = input("Pesquisa: ")

# Transform to url language, changing special characters
query_codificada = urllib.parse.quote(query, safe='')

# Makes the request GET
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+query_codificada+'&lang=pt')

# Requisition filter where text and user tweets are located in the dict and decode
decodificar = requisicao[1].decode()

# Transform the JSON data
objeto = json.loads(decodificar)

# Filter where text and users are located in dict
twittes = objeto['statuses']

# Shows screen name and text of which tweet
for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()

