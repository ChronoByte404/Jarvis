from AI.toolkit import *

class JarvisAI:
    def __init__(self, intents_file_path):
        self.ChatBot = chatbot(intents_file_path)

    def say(self, input_string):
        response = self.ChatBot.say(input_string)
        return response

    def get_class(self):
        intent_class = self.ChatBot.get_class()
        return intent_class
