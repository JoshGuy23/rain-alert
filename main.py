import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
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

sender = os.getenv("SENDER")
password = os.getenv("APP_PASSWORD")
if raining:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=os.getenv("RECEIVER"),
            msg="Subject:Rain Within 12 Hours\n\nIt is going to rain within the next 12 hours. "
                "Bring an umbrella."
        )
