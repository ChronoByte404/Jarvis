import os

class TTS:
    def say(text):
        os.system(f"'./Scripts/speech.sh' '{text}'")

if __name__ == "__main__":
    Voice = TTS()
    Voice.say("Hello, world. I am professor yana.")
