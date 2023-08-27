import requests
import json

class Basic:
    def __init__(self):
        self.url = "http://localhost:8000"

    def say(self, sentence):
        try:
            message_data = {"message": sentence}
            message_json = json.dumps(message_data)
            headers = {"Content-type": "application/json"}
            fullresponse = requests.post(self.url, data=message_json, headers=headers)
            ResponseOutput = fullresponse.text
            print(ResponseOutput)
        except:
            print("No response found.")
