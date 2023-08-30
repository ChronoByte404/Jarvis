from AI.janex_utils import *
from AI.nltk_utils import *

class chatbot:
    def __init__(self, intents_file_path):
        self.intents = self.load(intents_file_path)
        self.msc = None

    def load(self, intents_file_path):
        with open(intents_file_path, "r") as file:
            data = json.load(file)
        return data

    def say(self, input_string):
        most_similar_class = None
        meanings, sentence_meanings, highest_similarity = [], [], 0
        tokens = tokenize(input_string)
        for token in tokens:
            meaning = get_meaning(token)
            if not meaning:
                meaning = vectorize(token)
                meaning = f"{meaning}"
            meanings.append(meaning)
        for intent_class in self.intents["intents"]:
            for sentence in intent_class["sentences"]:
                sentence_tokens = tokenize(sentence)
                for token in sentence_tokens:
                    meaning = get_meaning(token)
                    if not meaning:
                        meaning = vectorize(token)
                        meaning = f"{meaning}"
                    sentence_meanings.append(meaning)

            similarity = compare_lists(meanings, sentence_meanings)
            if similarity > highest_similarity:
                print(similarity)
                most_similar_class = intent_class
                highest_similarity = similarity
                self.most_similar_class = most_similar_class

        if most_similar_class is not None:
            responses = most_similar_class['sentences']
            response = random.choice(responses)
            response = alter_sentence(response)
            return response
        else:
            for intent_class in self.intents["intents"]:
                sentence = random.choice(intent_class["sentences"])
                sentence_vectors = vectorize(sentence)
                input_vectors = vectorize(input_string)
                similarity = cosine_similarity(sentence_vectors, input_vectors)
                if similarity > highest_similarity:
                    highest_similarity = similarity
                    most_similar_class = intent_class
                    self.most_similar_class = most_similar_class
            responses = most_similar_class['sentences']
            response = random.choice(responses)
            response = alter_sentence(response)
            return response

    def get_class(self):
        return self.most_similar_class
