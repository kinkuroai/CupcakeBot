import discord
import asyncio
import os
import logging
import utils
from discord.ext import commands
from dotenv import load_dotenv

"""
I want to keep main.py really minimal so transferring some stuff to utils.py
Also planning to migrate to toml as a dotenv replacement - seems a lot cleaner.
"""

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

# The Bot
bot = commands.Bot(command_prefix=utils.get_prefix, description=BOT_DESCRIPTION, intents=utils.intents, activity=discord.Game(name=BOT_ACTIVITY))

# Stuff to load
to_load = [utils.load_extensions(bot), utils.load_helpers(bot)]

# Setup logging (set level to logging.DEBUG for more verbose stuff)
handler_info = logging.FileHandler('discord_info.log', encoding='utf-8', mode='w')
discord.utils.setup_logging(level=logging.ERROR, handler=handler_info, root=True)
discord.utils.setup_logging(level=logging.INFO, handler=handler_info, root=True)

# Running the bot
@bot.event
async def setup_hook():
    print(f'Logged in as: {bot.user.name}')
    print("Bot successfully connected!\n")

# Running the bot
async def main():
    async with bot:
        print("==================\nEXTENSIONS AND HELPERS\n==================\n")
        for exts in to_load:
            await exts
        print("\n==================\nEXTENSION AND HELPERS\n==================\n")
        await bot.start(BOT_TOKEN)

asyncio.run(main())