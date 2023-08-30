from textgenrnn import textgenrnn

# Train the model
textgen = textgenrnn.TextgenRnn()
textgen.train_from_file('waters_of_mars.txt', num_epochs=10)

# Generate text
generated_text = textgen.generate(return_as_list=True)[0]
print(generated_text)
