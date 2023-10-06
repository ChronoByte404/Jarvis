from gpt4all import GPT4All
from Janex import *
from JanexPT import *
from Utilities.functions import *

settings = loadconfig("./Settings/configuration.json")

class JarvisAI:
    def __init__(self):
        self.classifier = JanexPT("AI/intents.json")
        self.classifier.modify_data_path("BinaryFiles/data.pth")
        self.previous_input = None
        self.response_check()
        self.classifier.device = torch.device('cpu')
        self.gpt = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")

    def say(self, input_string):
        self.response_check()
        answer = input_string
        self.previous_input = input_string
        if self.response_setting == "random":
            intent_class = self.get_class()
            context = intent_class.get("context")
            if context == "command":
                responses = intent_class["responses"]
                response = random.choice(responses)
                return response
            else:
                Response = self.gpt.generate(f'{settings.get("SystemPrompt")}\n ###User: {input_string} \n %1 \n ### Response: ', max_tokens=64)
                return Response
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
