import uuid
import json
import os
import sqlite3

json_file = os.open("game.json", os.O_APPEND | os.O_RDWR | os.O_CREAT)

conn = sqlite3.connect("C:\\Users\\omele\\AppData\\Local\\LGHUB\\settings.db")
cursor = conn.cursor()

query = "SELECT file FROM data"
cursor.execute(query)
data = cursor.fetchall()

data = data[0][0].split(b"\n")
for i in data:
    os.write(json_file, i + b"\n")

os.close(json_file)
#open json file and load it
with open('game.json') as json_file:
    data = json.load(json_file)

#generate guid
guid = uuid.uuid4()

name = input("enter game name : ")
path = input("enter game path : ")
icon = input("enter game icon path : ")

#add info to json into the application section,
#it must loook like this
# {
#     "applicationId": "ecc7d9ab-dfa8-4070-a7d8-8460187b496c",
#     "applicationPath": "C:\\XboxGames\\The Elder Scrolls V- Skyrim Special Edition (PC)\\Content\\SkyrimSE.exe",
#     "isCustom": true,
#     "name": "Skyrim",
#     "posterPath": "c:\\Users\\omele\\AppData\\Local\\LGHUB\\icon_cache\\53306-1.jpg"
# },

data["applications"]["applications"].append({"applicationId": str(guid), "applicationPath": path, "isCustom": True, "name": name, "posterPath": icon})

#write the new json to the file
with open('game.json', 'w') as outfile:
    json.dump(data, outfile)

#read the json file and write it to the database
with open('game.json') as json_file:
    data = json_file.read()

query = "UPDATE data SET file = ?"

cursor.execute(query, (data,))

conn.commit()
os.remove("game.json")