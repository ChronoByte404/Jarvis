import requests
import json

class Basic:
    def __init__(self):
        self.url = "http://localhost:8000"
        self.intent_class = None

    def say(self, sentence):
        try:
            message_data = {"message": sentence}
            message_json = json.dumps(message_data)
            headers = {"Content-type": "application/json"}

            # Send a POST request to the server
            fullresponse = requests.post(self.url, data=message_json, headers=headers)

            # Check if the response status code is 200 (OK)
            if fullresponse.status_code == 200:
                # Parse the JSON response from the server
                response_data = json.loads(fullresponse.text)
                ResponseOutput = response_data.get('response', '')
                intent_class = response_data.get('intent_class', '')
                self.intent_class = intent_class

                # You can use ResponseOutput and intent_class as needed
                return ResponseOutput
            else:
                print(f"Error: Received status code {fullresponse.status_code}")
                return None, None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_class(self):
        ic = self.intent_class
        self.intent_class = None
        return ic
