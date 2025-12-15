import json
from datetime import datetime
mood = input("How do you feel today? ")
entry = {
    "date": str(datetime.now()),
    "mood": mood
}
try:
    with open("moods.json", "r") as file:
        data = json.load(file)
except:
    data = []
data.append(entry)
with open("moods.json", "w") as file:
    json.dump(data, file, indent=4)
print("Mood saved!")
