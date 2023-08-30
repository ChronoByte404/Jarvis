import tensorflow as tf
import numpy as np
import glob

file_paths = glob.glob("*.txt")  # This will get a list of all .txt files in the current directory

combined_text = ""

for file_path in file_paths:
    with open(file_path, "r") as file:
        content = file.read()
        combined_text += content
        print(file_path)

text = combined_text

chars = sorted(list(set(text)))
char_to_int = {ch:i for i, ch in enumerate(chars)}
int_to_char = {i:ch for i, ch in enumerate(chars)}

# Set the maximum sequence length (max_len) to be the length of the longest sequence
max_len = max([len(s) for s in text])

# Create training examples and labels
X = []
y = []

for i in range(0, len(text)-max_len, 1):
    X.append([char_to_int[ch] for ch in text[i:i+max_len]])
    y.append(char_to_int[text[i+max_len]])

# Pad the examples
X = tf.keras.preprocessing.sequence.pad_sequences(X, maxlen=max_len, padding='post')

# Convert labels to categorical format
y = tf.keras.utils.to_categorical(y)

# Define the model architecture
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim=len(chars), output_dim=64))
model.add(tf.keras.layers.LSTM(units=128))
model.add(tf.keras.layers.Dense(units=len(chars), activation='softmax'))

# Define optimizer and loss function
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss = 'categorical_crossentropy'

model.compile(optimizer, loss)

# Train the model
model.fit(X, y, epochs=100, batch_size=128)

model.save("Eureka.keras")

def generate_text(seed, num_chars):
    # Initialize the generated text
    generated_text = seed

    # Encode the seed as integers
    encoded_seed = [char_to_int[ch] for ch in seed]

    # Pad the seed
    padded_seed = tf.keras.preprocessing.sequence.pad_sequences([encoded_seed], maxlen=max_len, padding='post')

    # Generate characters
    for i in range(num_chars):
        # Get the next character probabilities
        probs = model.predict(padded_seed)[0]

        # Get the index of the character with the highest probability
        index = np.argmax(probs)

        # Add the character to the generated text
        generated_text += int_to_char[index]

        # Update the padded seed with the latest character
        padded_seed = np.append(padded_seed[0][1:], index)
        padded_seed = tf.keras.preprocessing.sequence.pad_sequences([padded_seed], maxlen=max_len, padding='post')

    return generated_text

# Generate text
generated_text = generate_text('water ', 100)
print(generated_text)
