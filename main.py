import discord
import asyncio
import os
import logging
import utils
import tomli
from discord.ext import commands
from dotenv import load_dotenv

"""
- I want to keep main.py really minimal so transferring some stuff to utils.py
- Migrated to TOML. Change the values in `config.toml.example` and rename it to `config.toml` for this bot to work.
"""

print("""
=============================================
████████████████████████████████████████████
█─▄▄▄─█▄─██─▄█▄─▄▄─█─▄▄▄─██▀▄─██▄─█─▄█▄─▄▄─█
█─███▀██─██─███─▄▄▄█─███▀██─▀─███─▄▀███─▄█▀█
▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
=============================================
""")

# Load config file
with open("config.toml", "rb") as c:
    config = tomli.load(c)

BOT_TOKEN = config['bot']['token']
BOT_ACTIVITY = config['bot']['activity']
BOT_DESCRIPTION = config['bot']['description']

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