import os

try:
    os.system("git pull")
except:
    os.system("git stash")
    os.system("git pull")