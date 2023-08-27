from toolkit import *

ChatBot = chatbot("intents.json")

input_string = input("You: ")
response = ChatBot.say(input_string)

print("Bot: ", response)
