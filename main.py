# Utilities

from Utilities.libraries import *
from Utilities.functions import *

# Interfaces

from Interfaces.discord import *
from Interfaces.whisper import *
from Interfaces.gui import *
from Interfaces.basic import *
from Interfaces.terminal import *

# AI Core

from AI.main import *

# Interface

config_data = loadconfig("AI/config.json")

def ChooseClient():
    ClientOption = input("Client: ")
    ClientOption = str(ClientOption)

    if "discord" in ClientOption:
        DiscordAPI = config_data.get("DiscordAPI")
        Bot = DiscordBot(DiscordAPI)
        Bot.activate_bot()
    elif "basic" in ClientOption:
        Bot = terminal_chat()
        while True:
            input_string = input("You: ")
            ResponseOutput = Bot.say(input_string)
            print(ResponseOutput)

if __name__ == "__main__":
    ChooseClient()
