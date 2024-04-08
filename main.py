import cmd
import data_manager as data
import system
from pytz import timezone
from datetime import datetime
from random import randint as randi
def _main():
    if data.user["setup"] == 0:
        data.setup()
    _greeting()
    while True:
        userInput = input(data.user["username"] + ": ").lower()
        if userInput == "exit":
            cmd.exit()
            break
        _listener(userInput)

def _greeting():
    t = datetime.now(timezone("America/New_York")).time()
    if t.strftime("%p") == "AM":
        msg = "morning"
    elif int(t.strftime("%I")) < 6:
        msg = "afternoon"
    else:
        msg = "evening"
    system.out(data.greetings[msg][randi(0, len(data.greetings[msg])-1)].replace("{user}", data.user["username"].strip("[]")))
    system.out("The time is " + str(t.strftime("%I:%M %p")))

def _listener(userInput):
    if userInput == "help" or userInput == "?":
        cmd.help()
    elif userInput == "setup":
        cmd.setup()
    elif userInput == "reset":
        cmd.reset()
    elif userInput == "save":
        cmd.save()
    else:
        system.out("Unrecognized command.\ntype help for a list of commmands.")

def _exit_process():
    ("[System Shutting Down]")

if __name__ == "__main__":
  _main()
_exit_process()
