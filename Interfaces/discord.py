import nextcord as discord
from nextcord.ext import commands

import requests
import json
from Interfaces.basic import *
from Utilities.functions import *

import nextcord
from nextcord.ext import commands

class DiscordBot:
    def __init__(self, DiscordAPI):
        self.DiscordAPI = DiscordAPI
        self.url = "http://localhost:8000"

        config_data = loadconfig("Settings/discord_key.json")
        settings = loadconfig("Settings/configuration.json")

        self.UIName = settings.get("UIName")
        self.Prefix = settings.get("Command_Prefix")

        # Set up intents with the required intents enabled
        self.discordintents = nextcord.Intents.default()
        self.discordintents.message_content = True
        self.client = commands.Bot(command_prefix='/', intents=self.discordintents)

        self.Basic = Basic()
        self.authorised_servers = settings.get("Authorised_Servers")
        self.authorised_users = settings.get("Authorised_Users")
        self.ResponseOutput = ""

    def activate_bot(self):
        @self.client.event
        async def on_message(message):
            if self.UIName in message.content or message.guild is None or message.reference and message.reference.resolved.author.bot:
                self.message = message
                self.user = message.author
                sentence = str(message.content)
                if message.author == self.client.user:
                    return
                sentence = str(sentence)
                ResponseOutput = self.Basic.say(sentence)
                self.ResponseOutput = ResponseOutput
                await message.reply(ResponseOutput)
                if message.author.name in self.authorised_users:
                    intent_class = self.Basic.get_class()
                    if intent_class:
                        DoFunction(intent_class)
            else:
                pass

        self.client.run(self.DiscordAPI)

if __name__ == "__main__":
    DiscordAPI = input("Discord token: ")
    Bot = DiscordBot(DiscordAPI)
    Bot.activate_bot()
