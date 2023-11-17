import nextcord as discord
from nextcord.ext import commands

import requests
import json
from Interfaces.basic import *
from Utilities.functions import *

import nextcord
from nextcord.ext import commands

import asyncio

class DiscordBot:
    def __init__(self, DiscordAPI):
        self.DiscordAPI = DiscordAPI
        self.url = "http://localhost:8000"

        config_data = loadconfig("Settings/discord_key.json")
        settings = loadconfig("Settings/configuration.json")
        self.settings = settings

        self.UIName = settings.get("UIName")
        self.Prefix = settings.get("Command_Prefix")

        # Set up intents with the required intents enabled
        self.discordintents = nextcord.Intents.default()
        self.discordintents.message_content = True
        self.client = commands.Bot(command_prefix='/', intents=self.discordintents)

        self.Basic = Basic()
        self.authorised_servers = settings.get("Authorised_Servers")
        self.authorised_users = settings.get("Authorised_Users")
        self.prefix = settings.get("Command_Prefix")

        self.ResponseOutput = ""

        with open('./Settings/JURISDICTION.json', 'r+') as file:
            data = json.load(file)
            self.incoming_servers = data['servers']

    def activate_bot(self):
        @self.client.event
        async def on_message(message):
            if self.UIName in message.content or message.guild is None or message.reference and message.reference.resolved.author == self.client.user:
                await message.channel.trigger_typing()

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
                
                mp3_tts(ResponseOutput)
                
                channel = self.client.get_channel(int('723270333523558455'))
                vc = nextcord.utils.get(self.client.voice_clients, guild=channel.guild)

                if not vc:
                    vc = await channel.connect()

                    if vc.is_playing():
                        vc.stop()
                    
                    source = await nextcord.FFmpegOpusAudio.from_probe("AudioFiles/audio.mp3", method="fallback")
                    vc.play(source)
            
            if message.author.guild_permissions.administrator:
                if self.prefix in message.content:
                    if "authorise" in message.content:
                        if str(message.guild) not in self.incoming_servers:
                            self.incoming_servers.append(str(message.guild))
                            dict = {"servers": self.incoming_servers}
                            with open('./Settings/JURISDICTION.json', "w") as file:
                                json.dump(dict, file, indent=4)
                            await message.reply(f"Server moderation for {message.guild} is now active.")
                        else:
                            self.incoming_servers = remove_from_list(str(message.guild), self.incoming_servers)
                            dict = {"servers": self.incoming_servers}
                            with open('./Settings/JURISDICTION.json', "w") as file:
                                json.dump(dict, file, indent=4)
                            await message.reply(f"Server moderation for {message.guild} is now deactivated.")
                    if "prune" in message.content:
                        if str(message.guild) not in self.incoming_servers:
                            await message.reply(f"Hmm. The {message.guild} server either isn't compatible with my pruning command, or I am not authorised to moderate this server.")
                        else:
                            member = message.mentions[0]
                            await member.ban()
                            await message.reply(f"{member} has been pruned successfully and relocated into the void.")

        async def on_member_join(member):
            servername = str(member.guild)
            if servername in self.incoming_servers:
                channel_id = self.incoming_servers[servername]
                channel = client.get_channel(channel_id)
                await channel.send(f"Hello, {member.name}! Welcome to the {servername} server!")

            role = discord.utils.get(member.guild.roles, name='Member')
            await member.add_roles(role)

        self.client.run(self.DiscordAPI)

if __name__ == "__main__":
    DiscordAPI = input("Discord token: ")
    Bot = DiscordBot(DiscordAPI)
    Bot.activate_bot()
