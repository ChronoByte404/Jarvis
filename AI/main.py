from JanexBot import *
from Janex import *
from JanexPT import *
from Utilities.functions import *

class JarvisAI:
    def __init__(self):
        self.chatbot = JanexBot("AI/database.json", "en_core_web_sm")
        self.classifier = JanexPT("AI/intents.json")
        self.previous_input = None
        self.response_check()

    def say(self, input_string):
        self.response_check()
        answer = input_string
        self.previous_input = input_string
        if self.response_setting == "random":
            IsQuestion = self.chatbot.CheckForQuestion(answer)
            if IsQuestion:
                answer = self.chatbot.give_answer(answer)
                return answer
            else:
                question = self.chatbot.ask_question(answer)
                self.chatbot.save_answer(answer)
                return question
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
