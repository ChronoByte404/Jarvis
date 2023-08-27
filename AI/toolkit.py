from AI.janex_utils import *
from AI.nltk_utils import *

class chatbot:
    def __init__(self, intents_file_path):
        self.intents = self.load(intents_file_path)

    def load(self, intents_file_path):
        with open(intents_file_path, "r") as file:
            data = json.load(file)
        return data

    def say(self, input_string):
        meanings, sentence_meanings, highest_similarity = [], [], 0
        tokens = tokenize(input_string)
        for token in tokens:
            meaning = get_meaning(token)
            meanings.append(meaning)
        for intent_class in self.intents["intents"]:
            for sentence in intent_class["sentences"]:
                sentence_tokens = tokenize(sentence)
                for token in sentence_tokens:
                    meaning = get_meaning(token)
                    sentence_meanings.append(meaning)

            similarity = compare_lists(meanings, sentence_meanings)
            if similarity > highest_similarity:
                most_similar_class = intent_class
                highest_similarity = similarity

        if most_similar_class:
            responses = most_similar_class['sentences']
            response = random.choice(responses)
            return response
