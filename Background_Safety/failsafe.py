import sys

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
