import json
import os
import sys
import webbrowser
from playsound import playsound
import pyttsx3
import threading

# Internal functions

def loadconfig(config_file_path):
    with open(config_file_path, "r") as json_file:
        config_data = json.load(json_file)
        return config_data

def saveconfig(file_path, dict):
    with open(file_path, 'w') as json_file:
        json.dump(dict, json_file, indent=4)

def play_notification_sound(sound_file_path):
    playsound(sound_file_path)

def play_sound_in_background(notification_sound_file):
    threading.Thread(target=play_notification_sound, args=(notification_sound_file,)).start()

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
    play_sound_in_background("AudioFiles/speechunderstood.mp3")
    intent_class = intent_class.get("tag")
    print(intent_class)
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
    elif intent_class == "change-response-type":
        change_response_setting()
    elif intent_class == "sleep-monitors":
        sleepPC()

OS = check_os()
# Website functions

def change_response_setting():
    settings_config = loadconfig("./Settings/configuration.json")
    if settings_config.get("response-type") == "random":
        settings_config["response-type"] = "fixed"
    else:
        settings_config["response-type"] = "random"
    saveconfig("./Settings/configuration.json", settings_config)

def open_google():
    webbrowser.open("https://www.google.co.uk")

def open_amazon():
    webbrowser.open("https://www.amazon.co.uk")

def open_youtube():
    webbrowser.open("https://www.youtube.co.uk")

def open_openai():
    webbrowser.open("https://chat.openai.co.uk")

def open_amazon_music():
    webbrowser.open("https://music.amazon.co.uk")

def open_twitter():
    webbrowser.open("https://www.twitter.co.uk")

def open_iplayer():
    webbrowser.open("https://www.bbc.co.uk/iplayer")

def open_disney_plus():
    webbrowser.open("https://www.disneyplus.co.uk/en-gb/select-profile")

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

def sleepPC():
    if OS == "Linux":
        print("Running on Linux")
        HostOS = "Linux"
        os.system("sleep 1; xset dpms force off")

def mute():
    if OS == "Linux":
        print("Running on Linux")
        HostOS = "Linux"
        os.system(f"amixer -D pulse sset Master 0%")

    elif OS == "MacOS":
        print("Running on macOS")
        os.system("osascript -e 'set Volume 0'")

def maxvol():
    if OS == "Linux":
        print("Running on Linux")
        HostOS = "Linux"
        os.system(f"amixer -D pulse sset Master 100%")

    elif OS == "MacOS":
        print("Running on macOS")
        os.system("osascript -e 'set Volume 10'")

engine = pyttsx3.init()

def speak(ResponseOutput):
    engine.say(ResponseOutput)
    engine.runAndWait()

def tts(ResponseOutput):
    threading.Thread(target=speak, args=(ResponseOutput,)).start()
