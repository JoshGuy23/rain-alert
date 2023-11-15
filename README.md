# Rain Alert

## Introduction

This program uses a weather API to determine if it will rain in the user's area within the next 12 hours, and if so, send the user an email.

## Setup

Before you start the program, it is important to do several things.

First, get your desired latitude and longitude from https://www.latlong.net/ and replace the respective values of LAT and LON within the program.

Second, you will need to get an App Password for the email account that will be sending the email. The steps on how to get this varies depending on the email client being used.

Third, you will need to get an API Key from https://openweathermap.org/ by creating a free account.

Then, follow the instructions on creating an environment file.

### Create an environment file

Create a separate file called "enviornment.env" and fill it in the following format, replacing the values in the quotes (but keeping the quotes):

APP_PASSWORD="your_app_password_here"

API_KEY="your_api_key"

SENDER="sending_email_address"

RECEIVER="email_address_receiving_email"

## Requirements

To run main.py, you will need the requests and dotenv packages, as well as the .env file you are instructed to create above.
