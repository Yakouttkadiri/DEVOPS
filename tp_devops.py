import requests
import os
import json


APIKEY = "240aa650f4db4e154a07d0459c30a347"
latitude = "5.902785"
longitude = "102.754175"
url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (latitude,longitude, APIKEY)
response = requests.get(url)
data = json.loads(response.text)
print(data)

 
