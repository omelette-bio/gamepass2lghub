import uuid
import json
import os

# # open json file and load it
# with open('games.json') as json_file:
#     data = json.load(json_file)

# #generate guid
# guid = uuid.uuid4()

# name = input("enter game name : ")
# path = input("enter game path : ")
# icon = input("enter game icon path : ")

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

