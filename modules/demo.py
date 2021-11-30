import json

import requests

class demo:
    def __init__(self):
        self.a = 4
        self.b = 5

    def GetResponseWeather(self,cityName,rapidapi_key):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q":cityName,"units":"metric"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': rapidapi_key
        }
        try:
         response = requests.request("GET", url, headers=headers, params=querystring)
         with open('response.json', 'wb') as outf:
             outf.write(response.content)

         data = json.loads(response.content)
         print("Miasto: " + data["name"])
         print("Temperatura: " + str(data["main"]["temp"]) + u'\xb0' + "C")
         print("Ciśnienie : " + str(data["main"]["pressure"]) + " hPa")
         print("Pogoda: {}".format(data["weather"][0]["main"]))
        except BaseException:
            print("złe miasto ")






