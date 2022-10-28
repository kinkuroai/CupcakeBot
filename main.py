import discord
import asyncio
import os
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
    try:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
    except:
        print("Loading Extensions failed!")

async def load_helpers():
    try:
        for filename in os.listdir("./helpers"):
            if filename.endswith(".py"):
                await bot.load_extension(f"helpers.{filename[:-3]}")
    except:
        print("Loading Helpers failed!")

bot = commands.Bot(command_prefix=get_prefix, description=BOT_DESCRIPTION, intents=intents, activity=discord.Game(name=BOT_ACTIVITY))

# Uhh.. Aesthetics..
spinner = Halo(text="Bot is currently running..", spinner="dots")

# Running the bot
@bot.event
async def setup_hook():
    print(f'Logged in as: {bot.user.name}')
    print("Bot successfully connected!\n")
    spinner.start()

# Stuff to load
to_load = [load_extensions(), load_helpers()]

# Setup logging (set level to logging.DEBUG for more verbose stuff)
handler_info = logging.FileHandler('discord_info.log', encoding='utf-8', mode='w')
discord.utils.setup_logging(level=logging.ERROR, handler=handler_info, root=True)
discord.utils.setup_logging(level=logging.INFO, handler=handler_info, root=True)

# Running the bot
async def main():
    async with bot:
        print("==================\nEXTENSIONS AND HELPERS\n==================\n")
        for exts in to_load:
            await exts
        print("\n==================\nEXTENSION AND HELPERS\n==================\n")
        await bot.start(BOT_TOKEN)

asyncio.run(main())