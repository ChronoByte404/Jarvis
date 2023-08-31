from JanexBot import *

class JarvisAI:
    def __init__(self):
        self.chatbot = JanexBot("AI/database.json", "en_core_web_sm")
    def say(self, input_string):
        answer = input_string
        IsQuestion = self.chatbot.CheckForQuestion(answer)
        if IsQuestion:
            answer = self.chatbot.give_answer(answer)
            return answer
        else:
            question = self.chatbot.ask_question(answer)
            self.chatbot.save_answer(answer)
            return question
