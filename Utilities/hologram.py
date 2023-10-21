import curses
import time
import json
from colorama import init, Fore
import os
from Utilities.functions import *

class NeuralHologram:
    def __init__(self):
        self.title = ""
        self.ResponseOutput = ""
        self.last_face = ""
        self.last_colour = ""

    def check_face_change(self):
        with open("./Short_Term_Memory/face.txt", "r") as f:
            recent_expression = f.read()

        if self.last_face != recent_expression:
            self.last_face = recent_expression
            return True
        else:
            return False
    
    def check_colour_change(self):
        settings = loadconfig("./Settings/configuration.json")

        colour = settings.get("colour")

        if self.last_colour != colour:
            self.last_colour = colour
            return True
        else:
            return False

    def display(self):
        settings = loadconfig("./Settings/configuration.json")

        colour = settings.get("colour")

        with open("./Utilities/face.json", "r") as f:
            data = json.load(f)
        
        faces = data["faces"]

        for face in faces:
            display = face["face"]
            tag = str(face.get("tag"))

            if tag == self.last_face:
                display_face = face["face"]
                if colour == "YELLOW":
                    for item in display_face:
                        print(Fore.YELLOW + item)
                elif colour == "RED":
                    for item in display_face:
                        print(Fore.RED + item)
                elif colour == "BLUE":
                    for item in display_face:
                        print(Fore.BLUE + item)

                break

    def activate(self):
        while True:
            if self.check_face_change() or self.check_colour_change():
                os.system("clear")
                self.display()
            time.sleep(0.5)

if __name__ == "__main__":
    Hologram = NeuralHologram()
    Hologram.activate()
