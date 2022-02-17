import requests, os, weather
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

lat = os.environ.get('LAT')
lon = os.environ.get('LON')
key = os.environ.get('WEATHER_API_KEY')
part = "current,minutely,daily,alerts"

url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}&units=imperial"

req = requests.get(url)

data = req.json()

def checkTemps():
    for x in range(24):
        temp = data['hourly'][x]['temp']
        print(temp)
        if temp <= 18:
            return True
        else:
            continue

def getLowestTemp():
    low = 100
    for x in range(24):
        temp = data['hourly'][x]['temp']
        if temp < low:
            low = temp
        else:
            continue
    return low
