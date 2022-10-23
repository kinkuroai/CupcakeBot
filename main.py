import discord
import typing
import asyncio
import os, time
import logging
from discord.ext import commands
from dotenv import load_dotenv
from halo import Halo

load_dotenv()

print("""
=============================================
████████████████████████████████████████████
█─▄▄▄─█▄─██─▄█▄─▄▄─█─▄▄▄─██▀▄─██▄─█─▄█▄─▄▄─█
█─███▀██─██─███─▄▄▄█─███▀██─▀─███─▄▀███─▄█▀█
▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
=============================================
""")

# dotenv stuff
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_ACTIVITY = os.getenv("BOT_ACTIVITY")
BOT_DESCRIPTION = os.getenv("BOT_DESCRIPTION")

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

def get_prefix(bot, message):
    # The bot's prefixes
    prefixes = ['?', "!"]
    return commands.when_mentioned_or(*prefixes)(bot, message)

# Load extensions and helpers
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def load_helpers():
    for filename in os.listdir("./helpers"):
        if filename.endswith(".py"):
            await bot.load_extension(f"helpers.{filename[:-3]}")

bot = commands.Bot(command_prefix=get_prefix, description=BOT_DESCRIPTION, intents=intents)

spinner = Halo(text="Bot is currently running..", spinner="dots")

# Running the bot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=BOT_ACTIVITY))
    print(f'Logged in as: {bot.user.name}({bot.user.id})')
    print("Bot successfully connected!\n")
    spinner.start()

to_load = [load_extensions(), load_helpers()]

async def main():
    async with bot:
        print("==================\nEXTENSIONS AND HELPERS\n==================\n")
        for i in to_load:
            await i
        print("\n==================\nEXTENSION AND HELPERS\n==================\n")
        await bot.start(BOT_TOKEN)

asyncio.run(main())