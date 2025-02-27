import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="echo", description="Echo a message to a channel")
    async def echo(self, interaction: discord.Interaction, message: str, channel: discord.TextChannel):
        channel = await interaction.guild.fetch_channel(channel.id)
        await channel.send(message)

    @app_commands.command(name="echo-embed", description="Echo an embed to a channel")
    async def echo_embed(self, interaction: discord.Interaction, message: str, channel: discord.TextChannel):
        try:
            channel = await interaction.guild.fetch_channel(channel.id)
            embed = discord.Embed(description=message, color=discord.Color.dark_purple())
            await channel.send(embed=embed)
        
        except discord.DiscordException as e:
            print(f"Error: {e}")


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=discord.Intents.default())

    async def setup_hook(self):
        await self.add_cog(General(self))

    async def on_ready(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")