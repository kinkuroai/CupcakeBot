import discord
import os
import tomli
from discord.ext import commands

"""
Will transfer all utility stuff here
"""

with open("config.toml", "rb") as c:
    print("Loaded config!")
    config = tomli.load(c)

# Bot Variables
BOT_TOKEN = config['bot']['token']
BOT_ACTIVITY = config['bot']['activity']
BOT_DESCRIPTION = config['bot']['description']

# API Keys
CUTTLY_KEY = config['keys']['cuttly_key']

# Random channel stuff
WELCOME_CHANNEL = config['vars']['welcome_channel']
AUTOROLE_NAME = config['vars']['autorole_name']

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