# Library
import requests
    # Interacting with web requests
#import json
    # What does JSON do?/ It exchanges data from servers or APIs which we need because we are fetching data from the OpenWeather API
    
# WEATHER KEY AND LOCATION IN LATITIUDE AND LONGITITUDE
API_KEY = "6a5a102342ed8586f196703367f9e2f5"

# URL

url = "http://api.openweathermap.org/data/2.5/weather?lat=38.47&lon=-121.36&appid=6a5a102342ed8586f196703367f9e2f5&units=imperial"

# Make the request
# REQUESTS

response = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=38.45&lon=-121.35&appid=6a5a102342ed8586f196703367f9e2f5&units=imperial")
data = response.json()
#BRUHHHH I MISSED THE PARENTHESES AFTER TEXT IN LINE 18


#MAKE FUNCTION PRINT EVERYTHING

#print(json.dumps(data, indent = 3))

temp= data ["main"]["temp"]
feels_like = data ["main"]["feels_like"]
Visibillity = data["visibility"]
condition_id = data ["weather"][0]["id"]
condition_word = data["weather"][0]["main"]
# What do the brackets mean?
    #USED TO LOOK UP VALUE IN LIST
# What does the 0 do?
    # FETCHES DATA FROM ITEMS

print(f"Temprature: {temp}")
print(f"It feels like: {feels_like}")
print(f"Visibillity: {Visibillity} meters")
print(f"Condition ID: {condition_id}")
print(f"Condition Word: {condition_word}")

#I need to change the way its formated to just round to the nearest integer.

def get_icon_name(condition_id):
    if condition_id == 800:
        return "Sunny"
    elif 801 <= condition_id <= 804:
        return "Cloudy"
    elif 500 <= condition_id <= 531:
        return "Rain"
    elif 200 <= condition_id <= 232:
        return "Thunder"
    else:
        return "Cloudy"
    
icon_name = get_icon_name(condition_id)

print(f"Icon to use: {icon_name}")

# Test it with some other codes to verify
print(f"Code 800 maps to: {get_icon_name(800)}")
print(f"Code 500 maps to: {get_icon_name(500)}")
print(f"Code 200 maps to: {get_icon_name(200)}")
print(f"Code 803 maps to: {get_icon_name(803)}")
    
    
    
    