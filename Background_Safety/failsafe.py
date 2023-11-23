import sys
import os

def check_settings():
    required_files = ["configuration.json", "discord_key.json", "JURISDICTION.json", "intents.json", "reminders.json"]
    for file in required_files:
        file_path = f"./Settings/{file}"
        if os.path.exists(file_path) is False:
            os.system(f"curl -o {file_path} https://raw.githubusercontent.com/Cipher58/Jarvis/main/Templates/{file}")
        else:
            print(f"{file_path} exists.")

def ShutdownSafely():
    fail = [
    "              ▄▄███████▄▄",
    "           ▄██▀░░░░░░░░░▀██▄",
    "          ██░░░░░░░░░░░░░░░██",
    "        ▄██░░░░░░░░░░░░░░░░░██▄",
    "       ██░░░░░XXX ░░░░░XXX░░░░██",
    "      ██░░░░░░XXXXX░░░XXX░░░░░░██",
    "    ████░░░░░░░░░░░░░░░░░░░░░░░████",
    "   ██ ██░░░░▄█████████████▄░░░░██ ██",
    "  ██   ██░░░██░░░░░░░░░░░██░░░██   ██",
    "  ██    ▀██░░░░░░░░░░░░░░░░░██▀    ██",
    "  ██      ▀██▄░░░░░░░░░░░▄██▀      ██",
    "  ████       ▀▀█████████▀▀        ████",
    "               ██     ██",
    "               ██     ██",
    "               ██     ██",
    "             ▄██▀     ▀██▄"]
    for item in fail:
        print(item)
    print("💾 My thread processes are stopping. I'm closing down.")
    print("💾 A fatal internal error has occurred and this program will now shut down to prevent damage.")
    sys.exit()

print("Backend protection online.")