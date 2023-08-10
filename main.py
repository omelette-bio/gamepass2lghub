import uuid
import json
import os
import sys
import sqlite3

json_file = os.open("game.json", os.O_APPEND | os.O_RDWR | os.O_CREAT)


print("warning : this script will overwrite the settings.db file, please make a backup of these files before continuing")
print("also for this to work, close completely logitech g hub")
print("press ENTER to continue")
input()

db_path = input("enter the path to the settings.db file : ")

if os.path.exists(db_path) == False:
    print("file not found")
    sys.exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = "SELECT file FROM data"
cursor.execute(query)
data = cursor.fetchall()

data = data[0][0].split(b"\n")
for i in data:
    try :
        os.write(json_file, i + b"\n")
    except:
        print("error while writing to file")
        sys.exit(1)

os.close(json_file)
#open json file and load it
with open('game.json') as json_file:
    data = json.load(json_file)

#generate guid
guid = uuid.uuid4()

name = input("enter game name : ")
path = input("enter game path : ")
icon = input("enter game icon path : ")

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