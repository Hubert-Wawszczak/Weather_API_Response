import json

import requests

class demo:
    def __init__(self):
        self.a = 4
        self.b = 5

    def GetResponseWeather(self,cityName):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q":cityName,"units":"metric"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "7501b24147mshd595fc8f2e5ac13p19fdf6jsnc5d0718ed300"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        with open('response.json', 'wb') as outf:
            outf.write(response.content)

        data = json.loads(response.content)
        print("Miasto: " + data["name"])
        print("Temperatura: " + str(data["main"]["temp"]) + u'\xb0'+"C")
        print("Ciśnienie : " + str(data["main"]["pressure"]) + " hPa")





