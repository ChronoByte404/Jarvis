from Janex import *
import numpy as np

progressive_verbs = {
    "go": "Going",
    "open": "Opening"
}

def word_tokenize(input_string):
    words = tokenize(input_string)
    return words

def cosine_similarity(vector1, vector2):
    # Resize vectors to a common dimension
    target_dim = 300
    vector1 = np.resize(vector1, target_dim)
    vector2 = np.resize(vector2, target_dim)

    # Calculate cosine similarity between two vectors
    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)

    if norm_vector1 == 0 or norm_vector2 == 0:
        return 0  # Handle zero division case

    similarity = dot_product / (norm_vector1 * norm_vector2)
    return similarity

def token_compare(sentence1, sentence2):
    common = 0
    sentence1tokens = tokenize(sentence1)
    sentence2tokens = tokenize(sentence2)

    length1 = len(sentence1tokens)
    length2 = len(sentence2tokens)
    totallength = length1 + length2

    for token in sentence1tokens:
        if token in sentence2tokens:
            common += 1

    percentage = (common / totallength) * 100
    return percentage

def compare_lists(list1, list2):

    common = 0

    length1 = len(list1)
    length2 = len(list2)
    totallength = length1 + length2

    for item in list1:
        if item in list2:
            common += 1

    percentage = (common / totallength) * 100

    return percentage

def alter_sentence(string):
    stationary = ["open", "start", "run", "begin", "launch", "go"]
    new_string = []

    words = tokenize(string)
    print(words)

    for word in words:
        if word in stationary:
            new_word = f"{word}ing"
            if word.istitle():
                new_word = new_word.capitalize()
            new_string.append(f"{new_word}")
        else:
            new_word = word
            new_string.append(f"{new_word}")

    new_sentence = " ".join(new_string)
    new_sentence = f"{new_sentence.capitalize()}."
    return new_sentence

def vectorize(input_string):
    dimensions = len(input_string)
    vector = np.zeros(dimensions)

    for i, char in enumerate(input_string):
        if i >= dimensions:
            break
        vector[i] = ord(char)  # Get the ASCII value of the character

    return vector
