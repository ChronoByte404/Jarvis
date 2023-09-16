# Utilities

from Utilities.libraries import *
from Utilities.functions import *
from Utilities.server import *

# Interfaces

from Interfaces.discord import *
from Interfaces.whisper_client import *
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
            tts(ResponseOutput)
            print(ResponseOutput)
    elif "server" in ClientOption:
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, RequestHandler)
        print('8000')
        httpd.serve_forever()
    elif "whisper" in ClientOption:
        Bot = terminal_chat()
        VoiceInput = Audio()
        while True:
            try:
                VoiceInput.VoiceCommand()
                InputString = VoiceInput.speech()
                ResponseOutput = Bot.say(InputString)
                tts(ResponseOutput)
                print(ResponseOutput)
            except:
                print("No speech detected.")
                pass

if __name__ == "__main__":
    background_alarm_clock()
    ChooseClient()
