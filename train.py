from Janex.intentclassifier import *

Classifier = IntentClassifier()

Classifier.set_intentsfp("AI/intents.json")
Classifier.set_vectorsfp("AI/vectors.json")
Classifier.set_dimensions(300)

Classifier.train_vectors()
