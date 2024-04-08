import data_manager as data
import system

def help():
    system.out(
"""
- Help / ? - Display this menu.
- Exit - Shut down system.
"""
)

def setup():
    system.out("Re-entering Setup")
    data.setup()

def save():
    system.out("Saving user data")
    data.save_user_data()

def reset():
    system.out("Are you sure you would like to delete all user data?")
    response = ""
    while response != "y" and response != "n":
        response = input("(y/n): ")
    if response == "n":
        system.out("Terminating Reset Process")
        return
    data.user = data.reset_user_data()
    data.save_user_data()

def exit():
    system.out("Would you like to save before exiting?")
    response = ""
    while response != "y" and response != "n":
        response = input("(y/n): ")
    if response == "y":
        save()
        system.out("User data saved successfully")
    system.out("System shutting down")
