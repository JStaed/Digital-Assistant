import json
import system

with open("user_data.json", "r") as f:
    rawData = f.read()
user = json.loads(rawData)

with open("greeting_data.json", "r") as f:
    rawData = f.read()
greetings = json.loads(rawData)

def setup():
    system.out("--Welcome to System Setup--")
    system.out("Enter information into each prompt")
    user["username"] = "[" + input("{Username}: ") + "]"
    user["system_name"] = "[" + input("{System Name}: ") + "]"
    user["setup"] = 1
    save_user_data()

def save_user_data():
    with open("user_data.json", "w") as f:
        rawData = json.dumps(user, indent = 4)
        f.write(rawData)

def reset_user_data():
    return dict(
    setup = 0,
    username = "User",
    system_name = "[System]"
    )
