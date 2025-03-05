import discord, logging
from discord.ext import commands
from discord import app_commands

class Applications(commands.Cog):
    def __init__(self, client):
        self.client = client
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    @app_commands.command(name="setup", description="Start setting up your applications")
    async def setup(self, interaction: discord.Interaction):
        pass