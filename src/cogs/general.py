import discord
import logging
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    @app_commands.command(name="github", description="Get the GitHub link for TiesBot")
    async def github(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            await interaction.followup.send("Click [here](https://github.com/meilaleinalainen/TiesBot) for the GitHub link!")
        except discord.DiscordException as e:
            logging.error(e)
    @github.error 
    async def github_error(self, interaction: discord.Interaction, error):
        try:
            await interaction.response.send_message(f"Caught an unexpected error. Please contact Meila if this persists.")
            await interaction.channel.send(f"Error: {error}")
        except discord.DiscordException as e:
            logging.error(e)

    @app_commands.command(name="replit", description="Get the Replit link for TiesBot")
    async def replit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            await interaction.followup.send("Click [here](https://replit.com/@MeilaTF/TiesBot) for the Replit link!")
        except discord.DiscordException as e:
            logging.error(e)
    @github.error 
    async def replit_error(self, interaction: discord.Interaction, error):
        try:
            await interaction.response.send_message(f"Caught an unexpected error. Please contact Meila if this persists.")
            await interaction.channel.send(f"Error: {error}")
        except discord.DiscordException as e:
            logging.error(e)