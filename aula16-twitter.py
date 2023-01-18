import oauth2
import json
import urllib.parse

# Access parameters into Twitter
api_key = ['IH53HhQa7m5p3IAHfO6XDy5Cd']()hide
api_key_secret = 'y4LllRuAYN1UUI0tQGz5iAdpK3Hufyat05XDjEFvH3LwPC5imV'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKAylQEAAAAAYz%2By2svTozoFX3Q%2F68yMbWtefcg%3Djy7pqr7Xz56EC0yR5pFvG0AIJxOlP6dqbK9WPKUjzAxGtvLBjU'
access_token = '1615807020577218560-Iu71vg1Tdnf6TLMz2YJAvdzwRVpGCf'
access_token_secret = 'iUR7PpQCP4sgx2mHMNp3W1DZX81nPjRGWPwCx0bRPKLRQ'
client_id = 'azZ3YmMxWXlCN1c4NUpPdENHQjA6MTpjaQ'
client_secret = 'MY-SMlynR1MGNMwi_G-nNHhopVzPnwPKwaPTyYtZKxaNfWlqnI'

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

