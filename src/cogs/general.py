import discord, logging
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    @app_commands.command(name="github", description="Get the GitHub link for TiesBot")
    async def github(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message("Click [here](https://github.com/meilaleinalainengithub/TiesBot) for the GitHub link!")
        except discord.DiscordException as e:
            logging.error(e)