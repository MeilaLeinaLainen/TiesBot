import discord, logging
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    @app_commands.command(name="echo", description="Echo a message to a channel with TiesBot")
    @app_commands.describe(
        message="Message to send. If `copy` is True, input the message ID here.",
        channel="The channel where the message will be sent.",
        copy="Whether to copy an already sent message. Defaults to False.",
        delete_origin="Whether to delete the message to copy. Defaults to False."
    )
    async def echo(
        self, 
        interaction: discord.Interaction, 
        message: str = "...",  
        channel: discord.TextChannel = None,  
        copy: bool = False,
        delete_origin: bool = False
    ):
        """Sends a message to a channel."""
        if await interaction.user.get_role(1336300381441097771) is None:
            await interaction.channel.send("Failed to edit message. You need to be Manager to run this.")
            return

        try:
            if channel is None:
                channel = interaction.channel

            if copy:
                if message is not None:
                    message = await interaction.channel.fetch_message(int(message))
                else: 
                    logging.warning("/echo | Invalid Arguments")
                    await interaction.response.send_message("Failed to send message. Invalid arguments.", ephemeral=True)
                    return
                
            if delete_origin:
                await message.delete()

            await channel.send(message)

        except discord.DiscordException as e:
            logging.error(e)

    @app_commands.command(name="edit", description="Edit a message sent by TiesBot")
    @app_commands.describe(
        new_message="Message to edit to. If `is_id` is True, this shouldbe a message ID",
        old_message="ID of the message to edit.",
        is_id="Whether `new_message` is a message id or not.",
        delete_origin='Whether to delete the original message to avoid the "(edited)". Defaults to False.'
    )
    async def edit(
        self, 
        interaction: discord.Interaction, 
        old_message: str,
        new_message: str,
        is_id: bool = False,
        delete_origin: bool = False
    ):
        """Edits a message sent by TiesBot."""
        if await interaction.user.get_role(1336300381441097771) is None:
            await interaction.channel.send("Failed to edit message. You need to be Manager to run this.")
            return

        try:
            if new_message is None or old_message is None:
                logging.warning("/edit | Invalid Arguments")
                await interaction.response.send_message("Failed to edit message. Invalid arguments.", ephemeral=True)
                return
            
            old_message = await interaction.channel.fetch_message(int(old_message))  
            channel = old_message.channel
            if is_id:         
                new_message = await interaction.channel.fetch_message(int(new_message))

            if delete_origin:
                await old_message.delete()
                await channel.send(new_message.content)
            else:
                await old_message.edit(content=new_message.content)

        except discord.DiscordException as e:
            logging.error(e)


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=discord.Intents.default())

    async def setup_hook(self):
        await self.add_cog(General(self))

    async def on_ready(self):
        await self.tree.sync()
        print(f"Logged in as {self.user}")