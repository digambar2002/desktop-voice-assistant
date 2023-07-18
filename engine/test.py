import requests
import config


def weather(query):
    query = query.replace("weather", "")
    query = query.replace("of", "")
    query = query.replace("in", "")
    print(query)
    if query == "":
        city = config.CITY_NAME + " weather"
    else:
        city = query+" weather"

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": city}

    headers = {
        "X-RapidAPI-Key": "d68c7a4ca0mshfe7db0559a72ad6p1f118fjsnb3beeaa77aac",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json()['current']['feelslike_c'])


weather("weather in Jalgaon")
