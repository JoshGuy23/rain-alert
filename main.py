import requests
import os
import smtplib

API_KEY = os.environ["API_KEY"]
LAT = 32.557152
LON = -94.739410
# SAN_LAT = 29.424122
# SAN_LON = -98.493629
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"

parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()

hourly = data["hourly"]

# first_hour = hourly[0]["weather"][0]["id"]
# print(f"The code for the first hour is {first_hour}")

next_twelve_hours = hourly[:12]

weather_ids = [weather["weather"][0]["id"] for weather in next_twelve_hours]

raining = False
for weather in weather_ids:
    if weather < 700:
        raining = True

sender = "dwdeathwolf@gmail.com"
password = os.environ["APP_PASSWORD"]
if raining:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs="jhecker2001@gmail.com",
            msg="Subject:Rain Within 12 Hours\n\nIt is going to rain within the next 12 hours in San Antonio. "
                "Bring an umbrella."
        )
