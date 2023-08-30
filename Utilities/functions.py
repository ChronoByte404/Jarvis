import json
import os
import sys
import webbrowser

# Internal functions

def loadconfig(config_file_path):
    with open(config_file_path, "r") as json_file:
        config_data = json.load(json_file)
        return config_data

def check_os():
    if sys.platform.startswith('linux'):
        print(f"Linux-based Operating System Detected.")
        return "Linux"
    elif sys.platform.startswith('darwin'):
        print(f"Caution: MacOS-based Operating System detected.")
        return "MacOS"
    elif sys.platform.startswith('win'):
        print(f"Caution: MS-DOS-based Operating System detected.")
        return "Windows"
    else:
        print(f"Caution: Unknown Operating System detected: {sys.platform}")
        return "Unknown"

def DoFunction(intent_class):
    intent_class = intent_class.get("tag")
    if intent_class == "open-google":
        open_google()
    elif intent_class == "open-amazon":
        open_amazon()
    elif intent_class == "open-youtube":
        open_youtube()
    elif intent_class == "open-openai":
        open_openai()
    elif intent_class == "open-amazon-music":
        open_amazon_music()
    elif intent_class == "open-twitter":
        open_twitter()
    elif intent_class == "open-iplayer":
        open_iplayer()
    elif intent_class == "open-disney-plus":
        open_disney_plus()
    elif intent_class == "atom":
        open_atom()
    elif intent_class == "document":
        open_libreoffice()
    elif intent_class == "play-music":
        play_pause_music()
    elif intent_class == "pause-music":
        play_pause_music()
    elif intent_class == "next-music":
        next_music()
    elif intent_class == "previous-music":
        previous_music()

OS = check_os()
# Website functions

def open_google():
    webbrowser.open("https://www.google.com")

def open_amazon():
    webbrowser.open("https://www.amazon.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_openai():
    webbrowser.open("https://chat.openai.com")

def open_amazon_music():
    webbrowser.open("https://music.amazon.com")

def open_twitter():
    webbrowser.open("https://www.twitter.com")

def open_iplayer():
    webbrowser.open("https://www.bbc.co.uk/iplayer")

def open_disney_plus():
    webbrowser.open("https://www.disneyplus.com/en-gb/select-profile")

def open_atom():
    os.system("atom-dev")

def open_libreoffice():
    os.system("libreoffice")

# Media functions

def play_pause_music():
    if OS == "Linux":
        os.system("playerctl play-pause")
    else:
        print("Operating system is not supported!")

def next_music():
    if OS == "Linux":
        os.system("playerctl next")
    else:
        print("Operating system is not supported!")

def previous_music():
    if OS == "Linux":
        os.system("playerctl previous")
    else:
        print("Operating system is not supported!")
