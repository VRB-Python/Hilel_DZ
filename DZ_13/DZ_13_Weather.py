#Zavdannja 1
import requests
import json
from pprint import *

print("Exercise 1")
list_of_cities = ["Berlin", "Bern", "Oslo", "Ankara", "Paris", "London", "Bucharest", "Tallinn", "Madrid", "Rome"]
API_key = "8138f6ce1c2c7c6f87e542cb17b349e3"
average_temp_by_city = {}
for city_name in list_of_cities:
    weather_request = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
    result = weather_request.json()
    min_temp = result["main"]["temp_min"]
    max_temp = result["main"]["temp_max"]
    average_temp_by_city[city_name] = int((min_temp + max_temp) / 2) #round(((min_temp + max_temp) / 2),0)

for temp in average_temp_by_city:
    print(f"The avarage temperature in {temp} is {average_temp_by_city[temp]} K.")
print()