import requests
import os

url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"Maan Meri Jaan","type":"tracks","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"X-RapidAPI-Key": "d68c7a4ca0mshfe7db0559a72ad6p1f118fjsnb3beeaa77aac",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
items = response.json()['tracks']['items']

song = ""
for x in items:
	song = x['data']['id']
	break

print(song)
command = "start spotify:track:"+song
os.system(command)