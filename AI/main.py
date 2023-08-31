from JanexBot import *
from Janex import *

class JarvisAI:
    def __init__(self):
        self.chatbot = JanexBot("AI/database.json", "en_core_web_sm")
        self.classifier = IntentClassifier()
        self.classifier.set_intentsfp("AI/intents.json")
        self.classifier.set_vectorsfp("AI/vectors.json")
        self.classifier.set_dimensions(10)
        self.previous_input = None

    def say(self, input_string):
        answer = input_string
        self.previous_input = input_string
        IsQuestion = self.chatbot.CheckForQuestion(answer)
        if IsQuestion:
            answer = self.chatbot.give_answer(answer)
            return answer
        else:
            question = self.chatbot.ask_question(answer)
            self.chatbot.save_answer(answer)
            return question

    def train_intents(self):
        self.classifier.train_vectors()

    def get_class(self):
        input_string = self.previous_input
        intent_class = self.classifier.classify(input_string)
        return intent_class
