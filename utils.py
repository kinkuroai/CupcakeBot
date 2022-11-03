import discord
import os
from discord.ext import commands

"""
Will transfer all utility stuff here
"""

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

def get_prefix(bot, message):
    # The bot's prefixes
    prefixes = ['?', ">"]
    return commands.when_mentioned_or(*prefixes)(bot, message)

# Load extensions and helpers
async def load_extensions(bot):
    try:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
    except:
        print("Loading Extensions failed!")

async def load_helpers(bot):
    try:
        for filename in os.listdir("./helpers"):
            if filename.endswith(".py"):
                await bot.load_extension(f"helpers.{filename[:-3]}")
    except:
        print("Loading Helpers failed!")