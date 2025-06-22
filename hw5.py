import requests
import pandas as pd
from datetime import datetime

# 1

API_KEY = "89ee45256b0785828cd51a8a8f5e60de"
LAT = "50.4501"
LON = "30.5236"

url = f"http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&units=metric&cnt=168&appid={API_KEY}"
response = requests.get(url)
data = response.json()

print("Raw weather forecast data:")
print(data)

# 2

weather_data = []

for forecast in data["list"]:
    dt = datetime.utcfromtimestamp(forecast["dt"])
    temperature = forecast["main"]["temp"]
    wind_speed = forecast["wind"]["speed"]
    weather_data.append([dt, temperature, wind_speed])

df = pd.DataFrame(weather_data, columns=["Datetime", "Temperature", "Wind Speed"])

print("\nWeather data as a data frame:")
print(df)

# 3

# a

df["Datetime"] = pd.to_datetime(df["Datetime"])
df["Day"] = df["Datetime"].dt.day

next_3_days = df[df["Day"] <= (df["Day"].max() + 2)]

min_temp = next_3_days["Temperature"].min()
max_temp = next_3_days["Temperature"].max()
avg_temp = next_3_days["Temperature"].mean()

print(f"\nMinimum temperature for the next 3 days: {min_temp}°C")
print(f"Maximum temperature for the next 3 days: {max_temp}°C")
print(f"Average temperature for the next 3 days: {avg_temp}°C")

# b
avg_wind_speed = df["Wind Speed"].mean()

hours_above_avg_wind_speed = df[df["Wind Speed"] > avg_wind_speed].shape[0]

print(f"Hours with wind speed above average for the next 3 days: {hours_above_avg_wind_speed}")
