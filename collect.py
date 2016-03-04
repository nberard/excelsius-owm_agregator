#!/usr/bin/python3
# -*-coding:utf-8 -*

import requests
import json
from urllib import parse

endpoint = "http://api.openweathermap.org/data/2.5/"
uri = "group"
cities_file = "data/cities.json"
units = "metric"
token = "101f79b79f822b47d18d196e900a0601"

with open(cities_file) as cities_content:
    cities_objects = json.load(cities_content)
    ids = list(map(lambda x: str(x["id"]), cities_objects))
    print(ids)

parameters_string = parse.urlencode({"id": ",".join(ids), "units": units, "APPID": token})
url = endpoint + uri + "?" + parameters_string

temperatures_fetched = requests.get(url).json()
temperatures_to_index = {}
for city_temperature in temperatures_fetched["list"]:
    temperatures_to_index[city_temperature["name"]] = city_temperature["main"]["temp"]
print(temperatures_to_index)