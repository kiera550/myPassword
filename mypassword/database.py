#loads and saves users in the json file
import json
import os

USER_DATA_FILE = "data/users.json"
os.makedirs(os.path.dirname(USER_DATA_FILE), exist_ok=True)

#loads users from json file
def load_users():
    #if file does not exist, return empty dictionary
    if not os.path.exists(USER_DATA_FILE):
        return {}

    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except(json.JSONDecodeError, FileNotFoundError):
        print("Error: User data file is either corrupted or missing. Resetting now...")
        return {}

#saves users to a json file
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)