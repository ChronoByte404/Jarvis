from Janex import *

def word_tokenize(input_string):
    words = tokenize(input_string)
    return words

def cosine_similarity(one, two):
    similarity = calculate_cosine_similarity(one, two)
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
