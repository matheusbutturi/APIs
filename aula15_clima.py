import requests
import json

# Asks the city name to get the weather
cidade = input('Escreva sua cidade: ')

# Make a request in format GET
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=29a246b1b59f2718d4e4c81c23a8e5a9')

# Transform with JSON
tempo = json.loads(requisicao.text)

# Save the weather conditions
weather = tempo['weather'][0]['main']

# Translate to portuguese the weather variable
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = "q="+weather+"&target=pt&source=en"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "f4398ce278mshbc4927b2c66a01cp1e5b30jsna5d3d5dd0f84",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)
condicoes = json.loads(response.text)

# Transform the temperature from Kelvin to Celsius
a = float(tempo['main']['temp']) - 273.15

# Print the weather translated and temperature in Celsius
print('Condição do tempo: ', condicoes['data']['translations'][0]['translatedText'])
print('Temperatura: ',"%.1f" % a, 'ºC')