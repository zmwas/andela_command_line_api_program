import requests
import sys


def fetch_weather(city):
    # the url for accessing the open weather map api
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    # to get  temperature in celsius instead of fahrenheit
    units = "&units=metric"
    # the key for accessing the api
    api_key = "&APPID=33a91ecdf9c129e8ff426a359a854b44"

    r = requests.get(url + city + units + api_key)

    data = r.json()

    weather = data.get('weather')[0]['description']

    max_temparature = r.json().get('main')['temp_max']

    min_temperature = r.json().get('main')['temp_min']

    print(
            "The weather in " + city + " today will be " + weather + "\n" + "with highs of " + str(
                    max_temparature) + u'\N{DEGREE SIGN}' + "C" + " and lows of  " + str(
                min_temperature) + u'\N{DEGREE SIGN}' + "C" + "\n" + "Have a lovely day :)")
