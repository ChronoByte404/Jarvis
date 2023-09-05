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
        self.UIName = "Jarvis"

        # Set up intents with the required intents enabled
        self.discordintents = nextcord.Intents.default()
        self.discordintents.message_content = True

        self.client = commands.Bot(command_prefix='/', intents=self.discordintents)
        self.Basic = Basic()
        self.authorised_servers = ["A.R.U. Computing", "Depression & Anxiety", "Depression and Anxiety", "The Workshop ⚙"]
        self.authorised_users = ["cipher58"]

        self.setup_commands()

    def setup_commands(self):
        @self.client.command()
        @commands.has_permissions(ban_members=True)
        async def ban(ctx, member: nextcord.Member, *, reason=None):
            await member.ban(reason=reason)
            await ctx.send(f'Banned {member.mention}')

        @self.client.command()
        @commands.has_permissions(kick_members=True)
        async def kick(ctx, member: nextcord.Member, *, reason=None):
            await member.kick(reason=reason)
            await ctx.send(f'Kicked {member.mention}')

        @self.client.command()
        async def repeat(ctx, *, message):
            await ctx.send(message)

        @self.client.command()
        @commands.has_permissions(manage_roles=True)
        async def role(ctx, member: nextcord.Member, role: nextcord.Role):
            await member.add_roles(role)
            await ctx.send(f'Added {role.name} role to {member.mention}')

        @self.client.command()
        async def authorise(ctx, message):
            self.authorised_servers.append(message.author.guild)
            await message.reply(f"{message.author.guild} added to moderation list.")

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
