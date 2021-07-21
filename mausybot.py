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
    await ctx.send("Mishka Bot has been initialized!")

@bot.command()
async def dmme(ctx, *, args):
    await ctx.author.send("Hello there, " + ctx.author.name)

# ADMIN HELPER COMMANDS
@bot.command()
async def getchid(ctx, *, given_name=None):
    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    channel_id = channel.id
    text_channel = bot.get_channel(channel_id)
    await ctx.send(text_channel.mention + " ID is " + str(channel_id))

bot.run('token')