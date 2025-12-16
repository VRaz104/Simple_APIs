import json
import requests
from datetime import datetime
correct_city = False
mood = input("How do you feel today? ")
print("Mood saved!")
while correct_city==False: 
    city = input("Enter a city: ")
    if city=="":
        print("Please enter a valid city name.")
    else:
        correct_city=True
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
if response.status_code != 200:
    print("Error fetching data.")
data=response.json()    
temp = data["current_condition"][0]["temp_C"]
desc = data["current_condition"][0]["weatherDesc"][0]["value"]
entry = {
    "date": str(datetime.now()),
    "mood": mood,
    f"weather in {city}": temp,
    f"condition in {city}": desc
}
try:
    with open("moods_and_weather.json", "r") as file:
        data = json.load(file)
except:
    data = []
data.append(entry)
with open("moods_and_weather.json", "w") as file:
    json.dump(data, file, indent=4)