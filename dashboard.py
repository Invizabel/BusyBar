import datetime
import json
import random
import re
import requests
import string
import time
from busylib import BusyBar, types
from geopy.geocoders import Nominatim

# New York City, New York
lat = 40.730610
lon = -73.935242
timer = 0.25

with BusyBar("10.0.4.20") as bb:
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

            timer_count = timer # Setting it to timer fixes division by zero error
            while True:
                if timer_count / 60 >= 1:
                    break

                # Loop
                for i in range(len(data)):
                    time.sleep(timer)
                    timer_count += timer
                    out = data[i:i+12]

                    # Display statistics
                    bb.display_draw(
                        types.DisplayElements(
                            application_name="my-app",
                            elements=[
                                types.TextElement(
                                    id="status",
                                    type="text",
                                    color="cyan",
                                    x=4,
                                    y=4,
                                    text=out,
                                    font="normal",
                                    display=types.DisplayName.FRONT,
                                ),
                            ],
                        )
                    )

        except Exception as ERROR:
            print(ERROR)


