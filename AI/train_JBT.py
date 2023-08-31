from JanexBot import *

chatbot = JanexBot("database.json", "en_core_web_sm")

while True:
    chatbot.train()
