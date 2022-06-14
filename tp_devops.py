import requests
import os
import json


api_key = "240aa650f4db4e154a07d0459c30a347"
lat = "39.571625"
lon = "2.650544"
url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, cle_api)
response = requests.get(url)
data = json.loads(response.text)
print(data)

 


