import oauth2
import json
import urllib.parse

# Get the consumer and token (key/secret) params to access Twitter API
consumer_key = 'IH53HhQa7m5p3IAHfO6XDy5Cd'
consumer_secret = 'y4LllRuAYN1UUI0tQGz5iAdpK3Hufyat05XDjEFvH3LwPC5imV'

token_key = '1615807020577218560-Iu71vg1Tdnf6TLMz2YJAvdzwRVpGCf'
token_secret = 'iUR7PpQCP4sgx2mHMNp3W1DZX81nPjRGWPwCx0bRPKLRQ'

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
