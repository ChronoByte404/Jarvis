# Utilities

from Utilities.libraries import *
from Utilities.functions import *
from Utilities.server import *
from Utilities.hologram import *

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

Hologram = NeuralHologram()

def discord_function():
    DiscordAPI = config_data.get("DiscordAPI")
    Bot = DiscordBot(DiscordAPI)
    Bot.activate_bot()

def basic_function():
    Bot = terminal_chat()
    while True:
        input_string = input("You: ")
        ResponseOutput = Bot.say(input_string)
        tts(ResponseOutput)
        print(ResponseOutput)

def whisper_function():
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

def server_function():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('8000')
    httpd.serve_forever()

def all_function():
    threading.Thread(target=server_function, args=()).start()
    discord_function()

def ChooseClient():
    ClientOption = input("Client: ")
    ClientOption = str(ClientOption)
    Hologram.title = ClientOption.upper()
    if ClientOption.lower() != "basic":
        threading.Thread(target=Hologram.activate, args=()).start()

    if "discord" in ClientOption:
        discord_function()
    elif "basic" in ClientOption:
        basic_function()
    elif "server" in ClientOption:
        server_function()
    elif "whisper" in ClientOption:
        whisper_function()
    elif "all" in ClientOption:
        Hologram.switch_to_blue()
        all_function()

if __name__ == "__main__":
    background_alarm_clock()
    ChooseClient()
