import discord
import os
import tomli
import aiosqlite
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
BOT_PREFIX = config['bot']['prefix']

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
    prefixes = BOT_PREFIX
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

# DB STUFF
async def send_embed(ctx: commands.Context, t, *d):
    embed = discord.Embed(title=t, description=" ".join(d), colour=0x303FFF)
    embed.set_thumbnail(url=ctx.author.avatar)
    return await ctx.send(embed=embed)
