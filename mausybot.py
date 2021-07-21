import discord
from discord.ext import commands
from mal import *

desc = 'Just another Discord bot for personal use'
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', description=desc, intents=intents)

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name)
    print("Default Prefix set at: " + bot.command_prefix)
    print("Cupcake bot activated!")
    await bot.change_presence(activity=discord.Game(name="with Puchi's feelings."))

## USER COMMANDS
# Make Bot say something
@bot.command(pass_context=True)
async def say(ctx, *, args):
    await ctx.send("{0}".format(args))
    await ctx.message.delete()

# Search Anime on MAL
@bot.command()
async def anime(ctx, *, title):
    search = AnimeSearch(title)
    anires = search.results[0].mal_id
    anime = Anime(anires)
    emb = discord.Embed(title='{} - {}'.format(anime.title, anime.title_japanese), description=anime.synopsis, color=0x00ff00)
    emb.set_image(url=anime.image_url)
    emb.add_field(name="Score", value=anime.score, inline=True)
    emb.add_field(name="Episodes", value=anime.episodes, inline=True)
    emb.add_field(name="Status", value=anime.status, inline=True)
    emb.set_footer(text="via MAL - {}".format(anime.url), icon_url=anime.image_url)
    channel = bot.get_channel(865996369236066314)
    await channel.send(embed=emb)

## ADMIN HELPER COMMANDS
# Get Channel ID
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def getchid(ctx, *, given_name=None):
    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    channel_id = channel.id
    text_channel = bot.get_channel(channel_id)
    await ctx.send("Sending ID through DM..")
    await ctx.author.send(text_channel.mention + " ID is " + str(channel_id))

@getchid.error
async def getchid_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to do that.")

# Channel Purge
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Successfully cleaned.')
        await ctx.message.delete()

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to do that.")

## MAINLY FOR TESTING STUFF
# Reactions on embeds
@bot.command()
async def reactemb(ctx):
    emb = discord.Embed(title="Test", description="Test", color=0x00ff00)
    emb.add_field(name="Test", value="Test", inline=False)
    emb.add_field(name="Test", value="Test", inline=False)
    reactEmb = await ctx.channel.send(embed=emb)
    await reactEmb.add_reaction("❤️")

bot.run('token')