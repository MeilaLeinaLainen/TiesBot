import discord
from discord.ext import commands
from discord import app_commands
from math import floor
import logging
import json

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        self.config = self.read_config()
        self.WELCOME_CHANNEL = self.config["WELCOME_CHANNEL"]
        self.EMERGENCY_CHANNEL = self.config["EMERGENCY_CHANNEL"]

    def read_config(self):
        with open("config.json", "r") as file:
            return json.load(file)

    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer()
            await interaction.followup.send(f"Pong! :ping_pong: -- {floor((self.client.latency * 1000))}ms")
        except discord.DiscordException as e:
            logging.error(e)
    @ping.error
    async def ping_error(self, interaction: discord.Interaction, error):
        try:
            await interaction.response.send_message(f"Caught an unexpected error. Please contact Meila if this persists.")
            await interaction.channel.send(f"Error: {error}")
        except discord.DiscordException as e:
            logging.error(e)

    # GUILDS
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        pass

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        pass

    @commands.Cog.listener()
    async def on_guild_update(self, guild):
        pass

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        pass

    @commands.Cog.listener()
    async def on_guild_stickers_update(self, guild, before, after):
        pass

    @commands.Cog.listener()
    async def on_audit_log_entry_create(self, entry):
        pass

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        pass

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        pass

    # MEMBERS
    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        pass

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        pass

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        pass

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        pass

    # MESSAGES
    @commands.Cog.listener()
    async def on_message(self, message):
        pass

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        pass

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        pass

    # POLLS
    @commands.Cog.listener()
    async def on_poll_vote_add(self, user, answer):
        pass

    @commands.Cog.listener()
    async def on_poll_vote_remove(self, user, answer):
        pass

    # REACTIONS
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        pass

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        pass

    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):
        pass

    @commands.Cog.listener()
    async def on_reaction_clear_emoji(self, reaction):
        pass

    # ROLES
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        pass

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        pass

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        pass

    # THREADS
    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        pass

    @commands.Cog.listener()
    async def on_thread_join(self, thread):
        pass

    @commands.Cog.listener()
    async def on_thread_update(self, before, after):
        pass

    @commands.Cog.listener()
    async def on_thread_remove(self, thread):
        pass

    @commands.Cog.listener()
    async def on_thread_delete(self, thread):
        pass

    @commands.Cog.listener()
    async def on_thread_member_join(self, member):
        pass

    @commands.Cog.listener()
    async def on_thread_member_remove(self, member):
        pass

    # VOICE
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        pass