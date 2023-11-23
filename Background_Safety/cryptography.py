import os
import json

# Function to encrypt JSON data into a list of ASCII values
def encrypt_to_numbers(data):
    encrypted_data = [ord(char) for char in json.dumps(data)]
    return encrypted_data

# Function to decrypt the encrypted list of ASCII values back to JSON data
def decrypt_from_numbers(encrypted_data):
    decrypted_data = json.loads(''.join(chr(char) for char in encrypted_data))
    return decrypted_data

# Function to encrypt a JSON file
def encrypt_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    encrypted_data = encrypt_to_numbers(data)
    with open(file_path, 'w') as file:
        json.dump(encrypted_data, file)

# Function to decrypt a JSON file
def decrypt_json_file(file_path):
    with open(file_path, 'r') as file:
        encrypted_data = json.load(file)
    decrypted_data = decrypt_from_numbers(encrypted_data)
    with open(file_path, 'w') as file:
        json.dump(decrypted_data, file)

# Function to walk through directories and encrypt/decrypt JSON files
def process_directory(root_dir, operation):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                if operation == 'encrypt':
                    encrypt_json_file(file_path)
                    print(f"Encrypted: {file_path}")
                elif operation == 'decrypt':
                    decrypt_json_file(file_path)
                    print(f"Decrypted: {file_path}")

# Set your directory path
#directory_path = '/path/to/your/directory'

# Encrypt all JSON files in the directory and subdirectories
#process_directory(directory_path, 'encrypt')

# Decrypt all JSON files in the directory and subdirectories
# process_directory(directory_path, 'decrypt')