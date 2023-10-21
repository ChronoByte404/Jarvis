from Janex import *
from JanexPT import *
from JanexBot import *
from JanexNLG import *

from Utilities.functions import *

settings = loadconfig("./Settings/configuration.json")

class JarvisAI:
    def __init__(self):
        self.chatbot = JanexBot("AI/database.json", "en_core_web_sm")
        self.classifier = JanexPT("AI/intents.json")
        self.classifier.modify_data_path("BinaryFiles/data.pth")
        self.previous_input = None
        self.response_check()
        self.classifier.device = torch.device('cpu')
        self.NLG = NLG("en_core_web_md", "./BinaryFiles/janex.bin")

    def say(self, input_string):
        self.response_check()
        answer = input_string
        self.previous_input = input_string
        if self.response_setting == "random":
            intent_class = self.get_class()
            response = self.NLG.generate_sentence(input_string)
            return response
        else:
            intent_class = self.get_class()
            if intent_class:
                responses = intent_class["responses"]
                response = random.choice(responses)
                return response

    def get_class(self):
        input_string = self.previous_input
        intent_class = self.classifier.pattern_compare(input_string)
        return intent_class

    def response_check(self):
        self.settings = loadconfig("./Settings/configuration.json")
        self.response_setting = self.settings.get("response-type")
