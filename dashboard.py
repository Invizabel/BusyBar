import datetime
import json
import random
import re
import requests
import string
import time
from geopy.geocoders import Nominatim

# New York City, New York
lat = 40.730610
lon = -73.935242

while True:
    try:
        # Current Time
        now = re.findall(r"\d{1,2}:\d{1,2}", str(datetime.datetime.now()))[0]

        # Weather
        gather_weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}",timeout=10).text
        gather_weather = json.loads(gather_weather)["properties"]["forecastHourly"]
        weather = requests.get(gather_weather).text

        current_temperature = str(json.loads(weather)["properties"]["periods"][0]["temperature"]) + " F";
        current_forecast = json.loads(weather)["properties"]["periods"][0]["shortForecast"]
        current_wind = json.loads(weather)["properties"]["periods"][0]["windSpeed"] + " " + json.loads(weather)["properties"]["periods"][0]["windDirection"];

        # ISS
        user_agent = "".join([random.choice(string.ascii_letters + string.digits) for i in range(random.randint(8,35))])
        iss = requests.get("http://api.open-notify.org/iss-now.json",timeout=10).json()
        geolocator = Nominatim(user_agent=user_agent)
        latitude = iss["iss_position"]["latitude"]
        longitude = iss["iss_position"]["longitude"]
        location = geolocator.reverse((latitude, longitude), language="en")
        if location:
            iss = f'{location.raw["address"]["state"]}, {location.raw["address"]["country"]}'
        else:
            iss = "Ocean or uninhabited area"

        # Create data
        data = f"Time: {now} Weather: {current_forecast} {current_temperature} Wind: {current_wind} ISS: {iss}"

        out = {
                "application_name": "my_app",
                "led_notification_color": "#FF0000FF",
                "elements": [
                {
                    "id": "0",
                    "timeout": 60,
                    "align": "center",
                    "x": 16,
                    "y": 8,
                    "type": "text",
                    "text": data,
                    "font": "normal",
                    "color": "#FFFFFFFF",
                    "width": 128,
                    "scroll_rate": 1000,
                    "scroll_start_delay": 1000,
                    "scroll_repeat_delay": 2500,
                    "display": "front"
                }
                ]
            }

        requests.post("http://10.0.4.20/api/display/draw",json=out,timeout=10)

        time.sleep(60)

    except Exception as ERROR:
        print(ERROR)


