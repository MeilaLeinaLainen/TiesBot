import discord
import logging
import json
import re
from discord.ext import commands
from discord import app_commands

class Manager(commands.Cog):
    def __init__(self, client):
        self.client = client
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        self.config = self.read_config()
        self.MANAGER_ROLE = self.config["MANAGER_ROLE"]

    def read_config(self):
        with open("config.json", "r") as file:
            return json.load(file)

    @commands.command(name="echo", description="Echo a message to a channel with TiesBot")
    async def echo(
        self, 
        ctx: commands.Context, 
        *, message: str
    ):
        logging.debug(f"Received message: {message}")
        
        matches = re.findall(r'<(.*?)>', message)
        message_content = message.replace(".echo ", "").split("<")[0].strip()
        
        logging.debug(f"Extracted message content: {message_content}")
        logging.debug(f"Extracted matches: {matches}")
        
        channel = None

        if message_content.isdigit():
            try:
                message_content = await ctx.channel.fetch_message(int(message_content))
                message_content = message_content.content
            except discord.NotFound:
                logging.warning("Message not found.")
                await ctx.send("Message not found.")
                return
            except discord.DiscordException as e:
                logging.error(f"Error fetching message: {e}")
                await ctx.send(f"Error fetching message: {e}")
                return

        for match in matches:
            if match.startswith("chan:"):
                channel = match.split("chan:")[1]

        target_channel = discord.utils.get(ctx.guild.text_channels, name=channel) if channel else ctx.channel
        logging.debug(f"Target channel: {target_channel}")

        await target_channel.send(message_content)

    @echo.error
    async def echo_error(self, ctx: commands.Context, error):
        if isinstance(error, app_commands.CheckFailure):
            try:
                await ctx.reply("You do not have the required role to use this command.", ephemeral=True)
            except discord.DiscordException as e:
                logging.error(e)
        else:
            try:
                await ctx.reply(f"Caught an unexpected error. Please contact Meila if this persists.")
                await ctx.reply(f"Error: {error}")
            except discord.DiscordException as e:
                logging.error(e)

    @app_commands.command(name="bulk-echo", description="Echo up to 10 messages to a channel with TiesBot")
    @app_commands.describe(
        messages="Message to send. If `copy` is True, input the message ID here. Separate messages with a comma (no spaces).",
        channel="The channel where the message will be sent.",
        copy="Whether to copy an already sent message. Defaults to False."
    )
    async def bulk_echo(
        self, 
        interaction: discord.Interaction, 
        messages: str = None,  
        channel: discord.TextChannel = None,  
        copy: bool = False
    ):
        """Bulk-send up to 10 messages to a channel."""
        try:        
            target_channel = channel if channel else interaction.channel

            if messages is not None:
                message_list = [msg.strip() for msg in messages.split(",")]
                for message in message_list:
                    if copy:
                        try:
                            fetched_message = await interaction.channel.fetch_message(int(message))
                            message_content = fetched_message.content
                        except discord.NotFound:
                            logging.warning(f"/bulk-echo | Message ID {message} not found.")
                            await interaction.message.reply(f"Message ID {message} not found.", ephemeral=True)
                            continue
                        except discord.DiscordException as e:
                            logging.error(e)
                            await interaction.message.reply(f"Failed to fetch message ID {message}.", ephemeral=True)
                            continue
                    else:
                        message_content = message

                    await target_channel.send(message_content)
                await interaction.message.reply("Messages sent successfully.", ephemeral=True)
            else: 
                logging.warning("/bulk-echo | Invalid Arguments")
                await interaction.message.reply("Failed to send message. Invalid arguments.", ephemeral=True)
                return

        except discord.DiscordException as e:
            logging.error(e)
            await interaction.message.reply("An error occurred while sending messages.", ephemeral=True)

    @bulk_echo.error
    async def bulk_echo_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.CheckFailure):
            try:
                await interaction.response.send_message("You do not have the required role to use this command.", ephemeral=True)
            except discord.DiscordException as e:
                logging.error(e)
        else:
            try:
                await interaction.response.send_message(f"Caught an unexpected error. Please contact Meila if this persists.")
                await interaction.channel.send(f"Error: {error}")
            except discord.DiscordException as e:
                logging.error(e)

    @app_commands.command(name="edit", description="Edit a message sent by TiesBot")
    @app_commands.describe(
        new_message="The new message to replace the old one. If `copy` is True, input the message ID here.",
        old_message="Message ID OR reply the message to edit.",
        delete_origin='Whether to delete the original message to avoid the "(edited)". Defaults to False.'
    )
    async def edit(
        self, 
        interaction: discord.Interaction, 
        old_message: str,
        new_message: str,
        copy: bool = False,
        delete_origin: bool = False
    ):
        """Edit a message sent by TiesBot."""
        try:
            await interaction.response.defer()
            if interaction.user.get_role(1336300381441097771) is None:
                await interaction.message.reply("Failed to edit message. You need to be Manager to run this.")
                return

            if new_message is None or old_message is None:
                logging.warning("/edit | Invalid Arguments")
                await interaction.message.reply("Failed to edit message. Invalid arguments.", ephemeral=True)
                return
            
            old_message = await interaction.channel.fetch_message(int(old_message))  
            channel = old_message.channel

            if copy:
                if interaction.reference is not None or message == "...":
                    message = interaction.reference.message_id
                    message = await interaction.channel.fetch_message(int(message))
                elif message is not None:
                    message = await interaction.channel.fetch_message(int(message))
                else: 
                    logging.warning("/echo | Invalid Arguments")
                    await interaction.message.reply("Failed to send message. Invalid arguments.", ephemeral=True)
                    return

            if delete_origin:
                await old_message.delete()
                await channel.send(new_message.content)
                await interaction.message.reply("Message sent successfully!", ephemeral=True)
            else:
                await old_message.edit(content=new_message.content)

        except discord.DiscordException as e:
            logging.error(e)

    @edit.error
    async def edit_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.CheckFailure):
            try:
                await interaction.response.send_message("You do not have the required role to use this command.", ephemeral=True)
            except discord.DiscordException as e:
                logging.error(e)
        else:
            try:
                await interaction.response.send_message(f"Caught an unexpected error. Please contact Meila if this persists.")
                await interaction.channel.send(f"Error: {error}")
            except discord.DiscordException as e:
                logging.error(e)
