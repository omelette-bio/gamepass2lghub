from uuid import uuid4
import uuid, json, os, sys, sqlite3, signal, argparse

# !TODO : use the autofetch argument to automatically find the game executable path by searching in the registry auto-fetch-data.json
# !TODO : add a link to image to fetch and download images for the game icon

# define a function to exit the script when the user press CTRL+C or CTRL+Z
def exit_func(sig, frame):
    try:
        os.remove("game.json")
    except:
        pass
    sys.exit(0)


signal.signal(signal.SIGINT, exit_func)
signal.signal(signal.SIGTERM, exit_func)


# define arguments for the script
parser = argparse.ArgumentParser(
    description="add a game to the logitech g hub database"
)
parser.add_argument(
    "--auto-fetch-games",
    help="automatically fetch the game executable path",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--auto-fetch-settings",
    help="automatically fetch the settings.db path",
    action="store_true",
    default=False,
)
args = parser.parse_args()


def add_game(data, guid, name, path, icon):
    data["applications"]["applications"].append(
    {
        "applicationId": str(guid),
        "applicationPath": path,
        "isCustom": True,
        "name": name,
        "posterPath": icon,
    }
)

print(
    "warning : this script will overwrite the settings.db file, please make a backup of these files before continuing"
)
print("also for this to work, close completely logitech g hub")
print("press ENTER to continue")
input()

db_path = input("enter the path to the settings.db file : ")

if os.path.exists(db_path) == False:
    print("file not found")
    sys.exit(1)


# connection to database + query to get the json file
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = "SELECT file FROM data"
cursor.execute(query)
data = cursor.fetchall()


# create the json file
json_file = os.open("game.json", os.O_APPEND | os.O_RDWR | os.O_CREAT)

# and write the json to it
data = data[0][0].split(b"\n")
for i in data:
    try:
        os.write(json_file, i + b"\n")
    except:
        print("error while writing to file")
        os.close(json_file)
        os.remove("game.json")
        sys.exit(1)

data = json.load("game.json")

if args.auto_fetch == False:
    guid = uuid4()
    name = input("enter game name : ")
    path = input("enter game path : ")
    icon = input("enter game icon path : ")
    

add_game(data, guid, name, path, icon)

# write the new json to the file
with open("game.json", "w") as outfile:
    json.dump(data, outfile)

# read the json file and write it to the database
with open("game.json") as json_file:
    data = json_file.read()

query = "UPDATE data SET file = ?"

cursor.execute(query, (data,))

conn.commit()
os.remove("game.json")