import discord
from discord.ext import commands
import sys, traceback

BOT_TOKEN = 'TOKEN'

def get_prefix(bot, message):
    # The bot's prefixes
    prefixes = ['?', "$", "m!", "m>"]
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.basics', 'cogs.mods', 'cogs.owner']
desc = 'Just another personal discord bot.'

bot = commands.Bot(command_prefix=get_prefix, description=desc)

# Loading the extensions
if __name__ == '__main__':
    for ext in initial_extensions:
        bot.load_extension(ext)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name} - {bot.user.id}')
    await bot.change_presence(activity=discord.Game(name="a game."))
    print(f'C3Bot successfully booted!')

bot.run(BOT_TOKEN, bot=True, reconnect=True)