from Interfaces.basic import *
from Utilities.functions import *

class terminal_chat:
    def __init__(self):
        self.basic = Basic()

    def say(self, sentence):
        ResponseOutput = self.basic.say(sentence)
        intent_class = self.get_class()
        if intent_class:
            DoFunction(intent_class)
        return ResponseOutput

    def get_class(self):
        intent_class = self.basic.get_class()
        return intent_class
