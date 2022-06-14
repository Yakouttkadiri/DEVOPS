import requests
import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getWeather():
    args = request.args
    APIKEY = "240aa650f4db4e154a07d0459c30a347"
    latitude = "5.902785"
    longitude = "102.754175"
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (latitude,longitude, APIKEY)
    response = requests.get(url)
    data = json.loads(response.text)
    
    print(data)


if __name__ == "__main__":
    port=8081
    app.run(host="0.0.0.0", port=port, debug=True)
