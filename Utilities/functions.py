import json

def loadconfig(config_file_path):
    with open(config_file_path, "r") as json_file:
        config_data = json.load(json_file)
        return config_data
