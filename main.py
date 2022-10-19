import discord
import typing
import asyncio
import requests
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()

# dotenv stuff
BOT_TOKEN = os.getenv("BOT_TOKEN")
KAWAII_TOKEN = os.getenv("KAWAII_TOKEN")
BOT_ACTIVITY = os.getenv("BOT_ACTIVITY")

def get_prefix(bot, message):
    # The bot's prefixes
    prefixes = ['?', "m?"]
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

desc = 'Just another personal discord bot.'

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=get_prefix, description=desc, intents=intents)

# Sync command
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: typing.Optional[typing.Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

    await ctx.send(f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}")
    return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

# Running the bot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=BOT_ACTIVITY))
    print(f'Logged in as: {bot.user.name} - {bot.user.id}')
    print("Bot successfully connected!")

async def main():
    async with bot:
        await load_extensions()
        await load_helpers()
        await bot.start(BOT_TOKEN)

asyncio.run(main())
