#!/usr/bin/python3
# -*-coding:utf-8 -*

import requests
import os
import sys
import yaml
import datetime
from elasticsearch import Elasticsearch

from urllib import parse

base_dir = os.path.dirname(__file__)

endpoint = "http://api.openweathermap.org/data/2.5/"
uri = "group"
units = "metric"
config = yaml.safe_load(open(os.path.join(base_dir, "config.yml")))
token = config["open_weather_map"]["token"]

ids = list(map(lambda x: str(x["id"]), config["cities"]))

parameters_string = parse.urlencode({"id": ",".join(ids), "units": units, "APPID": token})
url = endpoint + uri + "?" + parameters_string

temperatures_fetched = requests.get(url).json()
temperatures_to_index = {}
connect_string = ":".join([config["elastic_search"]["host"], str(config["elastic_search"]["port"])])
es = Elasticsearch(connect_string)
now_date = datetime.datetime.now().isoformat()
for city_temperature in temperatures_fetched["list"]:
    body = {
        "date": now_date,
        "temperature": city_temperature["main"]["temp"],
        "owm_id": city_temperature["id"],
        "name": city_temperature["name"],
        "long": city_temperature["coord"]["lon"],
        "lat": city_temperature["coord"]["lat"],
        "humidity": city_temperature["main"]["humidity"]
    }
    response = es.create(index="excelsius", doc_type="temperature", body=body)
    if not response["created"]:
        print("unable to create: ", body, file=sys.stderr)
    else:
        print("successfully created: ", body)
