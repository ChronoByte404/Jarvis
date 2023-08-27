import nltk
nltk.download("wordnet")

from nltk.corpus import wordnet

def get_meaning(word):
    synsets = wordnet.synsets(word)
    meanings = []
    for synset in synsets:
        meanings.append(synset.definition())
    return meanings

if __name__ == "__main__":
    word = input("Input word: ")
    meanings = get_meaning(word)
    print(f"Meanings of '{word}':")
    if meanings:
        for i, meaning in enumerate(meanings, start=1):
            print(f"{i}: {meaning}")
    else:
        print(f"No meanings found for word '{word}'.")
