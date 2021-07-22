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
@bot.command()
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

# Search Manga on MAL
@bot.command()
async def manga(ctx, *, title):
    search = MangaSearch(title)
    manres = search.results[0].mal_id
    manga = Manga(manres)
    emb = discord.Embed(title='{} - {}'.format(manga.title, manga.title_japanese), description=manga.synopsis, color=0x00ff00)
    emb.set_image(url=manga.image_url)
    emb.add_field(name="Score", value=manga.score, inline=True)
    emb.add_field(name="Volumes", value=manga.volumes, inline=True)
    emb.add_field(name="Status", value=manga.status, inline=True)
    emb.set_footer(text="via MAL - {}".format(manga.url), icon_url=manga.image_url)
    channel = bot.get_channel(865996651906727977)
    await channel.send(embed=emb)

## MODERATOR COMMANDS
# Ban someome
@bot.command()
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason = reason)
    await ctx.send(f"{member} was banned for {reason}")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}, you do not have permission to do that.".format(ctx.author.mention))

# Unban someone || To Fix
@bot.command()
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, *, member):        
    if "#" in ctx.message.content:
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users: 
            member_name, member_discriminator = member.split('#')
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member} has been unbanned!")
            else:
                await ctx.author.send("You need a name and a discriminator to continue.")
    else:
        member = await bot.fetch_user(int(member))
        await ctx.guild.unban(member)
        await member.send("You have been unbanned from {ctx.guild.name}!")
        await ctx.send(f"{member} has been unbanned!")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}, you do not have permission to do that.".format(ctx.author.mention))

# Get ban list
@bot.command()
@commands.has_guild_permissions(ban_members=True)
async def getbans(ctx):
    bannedId = await ctx.guild.bans()
    print(bannedId)

@getbans.error
async def getbans_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}, you do not have permission to do that.".format(ctx.author.mention))

## ADMIN HELPER COMMANDS
# Get Channel ID
@bot.command()
@commands.has_permissions(administrator=True)
async def getchid(ctx, *, given_name=None):
    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    channel_id = channel.id
    text_channel = bot.get_channel(channel_id)
    await ctx.send("Sending ID through DM..")
    await ctx.author.send(text_channel.mention + " ID is " + str(channel_id))

@getchid.error
@commands.has_permissions(administrator=True)
async def getchid_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}, you do not have permission to do that.".format(ctx.author.mention))

# Channel Purge
@bot.command()
@commands.has_permissions(administrator=True)
async def purge(ctx):
        await ctx.channel.purge()
        await ctx.send('Successfully cleaned.')
        await ctx.message.delete()

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("{}, you do not have permission to do that.".format(ctx.author.mention))

## MAINLY FOR TESTING STUFF

bot.run('token')