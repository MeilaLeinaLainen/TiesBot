import discord, logging, json, os
from discord.ext import commands
from discord import app_commands

from src.cogs.general import General
from src.cogs.manager import Manager
from src.cogs.events import Events

#from src.cogs.utils.tiesbot_ai import TiesBotAi

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=discord.Intents.default())

    async def setup_hook(self):
        await self.add_cog(General(self))
        await self.add_cog(Manager(self))
        #await self.add_cog(Events(self))
        #await self.add_cog(TiesBotAi(self))

    async def on_ready(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")