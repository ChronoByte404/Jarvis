import nextcord as discord
import requests
import json

class DiscordBot:
    def __init__(self, DiscordAPI):
        self.DiscordAPI = DiscordAPI
        self.url = url = "http://localhost:8000"
        self.discordintents = discord.Intents.all()
        self.client = discord.Client(intents=self.discordintents)

    def activate_bot(self):

        @self.client.event
        async def on_message(message):

            sentence = str(message.content)

            if message.author == self.client.user:
                return

            UIName = "Jarvis"

            if UIName in sentence:

                sentence = str(sentence)

                message_data = {"message": sentence}
                message_json = json.dumps(message_data)
                headers = {"Content-type": "application/json"}
                fullresponse = requests.post(self.url, data=message_json, headers=headers)
                ResponseOutput = fullresponse.text
                await message.reply(ResponseOutput)

            else:
                pass

        self.client.run(self.DiscordAPI)

if __name__ == "__main__":
    DiscordAPI = input("Discord token: ")
    Bot = DiscordBot(DiscordAPI)
    Bot.activate_bot()
