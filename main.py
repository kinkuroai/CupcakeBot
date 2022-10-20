import discord
import typing
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import os
import logging

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
GUILD_ID = os.getenv("GUILD_ID")
AUTOROLE_ID = os.getenv("AUTOROLE_ID")
WELCOME_CHANNEL = os.getenv("WELCOME_CHANNEL")
DESCRIPTION = os.getenv("DESCRIPTION")

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

bot = commands.Bot(command_prefix=get_prefix, description=DESCRIPTION, intents=intents)

# Running the bot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=BOT_ACTIVITY))
    print(f'Logged in as: {bot.user.name}({bot.user.id})')
    print("Bot successfully connected!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name=WELCOME_CHANNEL)

    r = requests.get('https://api.waifu.im/random/?&gif=true')
    result = r.json()

    embed = discord.Embed(title="Hello there!", description=f"Welcome to the server, {member.mention}!")
    embed.set_image(url=result['images'][0]['url'])

    await channel.send(embed=embed)

    guild = client.get_guild(GUILD_ID)
    role = guild.get_role(AUTOROLE_ID)
    await member.add_roles(role)



async def main():
    async with bot:
        await load_extensions()
        print("""==================\nLoaded Extensions!\n==================""")
        await load_helpers()
        print("""==================\nLoaded Helpers!\n==================""")
        await bot.start(BOT_TOKEN)

asyncio.run(main())
