import requests, os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

city = os.environ.get('CITY')
state = os.environ.get('STATE')
key = os.environ.get('WEATHER_API_KEY')

url = f" http://pro.openweathermap.org/data/2.5/forecast/hourly?q={city},{state}&appid={key}&units=imperial"

req = requests.get(url)

data = req.json()

pprint(data)