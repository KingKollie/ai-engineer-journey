
import requests 

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)

    if response.status_code == 200:
       print(f"Weather report: {response.text}")
    else:
         print("could not get weather data.")

city = input("Enter a city Name: ")
get_weather(city)       