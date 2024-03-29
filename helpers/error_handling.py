import discord
import traceback
import sys
from discord.ext import commands
from discord import app_commands
import logging

logger = logging.getLogger('discord_info.log')

'''
Still need to add a lot of stuff in here.
'''

class CommandErrorHandler(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print("ErrorHandling Cog: Loaded!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # If command does not exist
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("`That command does not exist!`")
            logger.error(f"{ctx.author.display_name} entered an invalid command.")

        # If command is disabled
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("`That command is currently disabled!`")

        # If member is not found
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("`User does not exist!`")

        # If command-user doesn't have the necessary permissions
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("`You do not have the required permissions to use this command!`")
            logger.error(f"{ctx.author.display_name} tried to access something he's not supposed to.")
        
        # If Syncing fails
        elif isinstance(error, app_commands.CommandSyncFailure):
            await ctx.send(f"Failed to sync")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandErrorHandler(bot))
