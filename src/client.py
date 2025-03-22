import discord
import logging
import json 
import os
from discord.ext import commands
from discord import app_commands
from src.cogs.general import General
from src.cogs.manager import Manager
from src.cogs.events import Events

#from src.cogs.utils.tiesbot_ai import TiesBotAi

class Client(commands.Bot):
    def __init__(self):
        intents=discord.Intents.default()
        intents.messages = True
        super().__init__(command_prefix=".", intents=intents)

    async def setup_hook(self):
        await self.add_cog(General(self))
        await self.add_cog(Manager(self))
        await self.add_cog(Events(self))
        #await self.add_cog(TiesBotAi(self))

    async def on_ready(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        await self.process_commands(message)