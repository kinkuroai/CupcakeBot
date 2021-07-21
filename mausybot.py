import discord
from discord.ext import commands

desc = 'Just another Discord bot for personal use'
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', description=desc, intents=intents)

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name)
    print("Default Prefix set at: " + bot.command_prefix)
    print("Cupcake bot activated!")
   
@bot.command()
async def hello(ctx):
    await ctx.send("Hi there!")

bot.run('token')