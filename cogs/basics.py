import discord
import aiohttp
import random
import tomli
import utils
from discord.ext import commands

class Basics(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print('Basics Cog: Loaded!')

    # Make the bot say something
    @commands.hybrid_command(name="say", description="Make the bot say something.")
    @commands.guild_only()
    async def do_say(self, ctx: commands.Context, *, msg: str) -> None:
        await ctx.send(msg)
        await ctx.message.delete()
    
    # Slaps someone | I have something fun planned for it (expanding on it soon)
    @commands.hybrid_command(name="slap", description="Slap someone you hate or love")
    @commands.guild_only()
    async def do_slap(self, ctx: commands.Context, member: discord.Member) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.best/api/v2/slap') as r:
                result = await r.json()
                link = result['results'][0]['url']
                if r.status in {200, 201}:
                    embed = discord.Embed(title="Hey you!", description=f"{ctx.author.mention} slapped {member.mention} hard in the face!", colour=0xea213a)
                    embed.set_image(url=link)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("`Unable to process command at the moment`")
    
    # Hugs someone
    @commands.hybrid_command(name="hug", description="Hug someone you hate or love")
    @commands.guild_only()
    async def do_hug(self, ctx: commands.Context, member: discord.Member) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.best/api/v2/hug') as r:
                result = await r.json()
                link = result['results'][0]['url']
                if r.status in {200, 201}:
                    embed = discord.Embed(title="Sending love!", description=f"{ctx.author.mention} hugged {member.mention}!", colour=0xF77BEF)
                    embed.set_image(url=link)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("`Unable to process command at the moment`")
    
    # Calls someone baka!
    @commands.hybrid_command(name="baka", description="Call someone baka!")
    @commands.guild_only()
    async def do_baka(self, ctx: commands.Context, member: discord.Member) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.best/api/v2/baka') as r:
                result = await r.json()
                link = result['results'][0]['url']
                if r.status in {200, 201}:
                    embed = discord.Embed(title="Baka!", description=f"{ctx.author.mention} called {member.mention} baka!", colour=0xF77BEF)
                    embed.set_image(url=link)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("`Unable to process command at the moment`")
    
    # What the fuck is that person saying?
    @commands.hybrid_command(name="wtfys", description="WTF is that guy saying?")
    @commands.guild_only()
    async def do_wtfys(self, ctx: commands.Context, member: discord.Member) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.best/api/v2/facepalm') as r:
                result = await r.json()
                link = result['results'][0]['url']
                if r.status in {200, 201}:
                    embed = discord.Embed(title="WHUUUUT?!", description=f"What the f*** are you saying, {member.mention}?", colour=0xea213a)
                    embed.set_image(url=link)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("`Unable to process command at the moment`")
    
    # Shortens a URL. Cleaner this way.
    @commands.command(name="shorten", description="Shortens a link for you")
    @commands.is_owner()
    async def do_shorten(self, ctx, to_shorten):
        key = utils.CUTTLY_KEY
        async with aiohttp.ClientSession() as session:
            async with session.get('http://cutt.ly/api/api.php?key={}&short={}'.format(key, to_shorten)) as r:
                await ctx.message.delete()
                result = await r.json()
                if r.status in {200, 201}:
                    await ctx.send(result['url']['shortLink'])
                else:
                    await ctx.send("`Unable to process command at the moment`")
    
    # Summons a random waifu
    @commands.hybrid_command(name="waifu", description="Summon a waifu")
    @commands.guild_only()
    async def get_waifu(self, ctx: commands.Context, a: str) -> None:
        async with aiohttp.ClientSession() as session:

            tags_sfw = [
                "uniform",
                "maid",
                "waifu",
                "marin-kitagawa",
                "mori-calliope",
                "aiden-shogun",
                "oppai",
                "selfies"
            ]

            tags_nsfw = [
                "ass",
                "hentai",
                "milf",
                "oral",
                "paizuri",
                "ecchi",
                "ero"
            ]

            if a == 'nsfw':
                async with session.get(f'https://api.waifu.im/random/?selected_tags={random.choice(tags_nsfw)}') as r:
                    result = await r.json()
                    waifu_image = result['images'][0]['url']
                    if r.status in {200, 201}:
                        await ctx.send(waifu_image)
                    else:
                        await ctx.send("`Unable to process command. Please try again.`")
            elif a == 'sfw':
                async with session.get(f'https://api.waifu.im/random/?selected_tags={random.choice(tags_sfw)}') as r:
                    result = await r.json()
                    waifu_image = result['images'][0]['url']
                    if r.status in {200, 201}:
                        await ctx.send(waifu_image)
                    else:
                        await ctx.send("`Unable to process command. Please try again.`")
    
    # Just some random facts you may not know
    @commands.hybrid_command(name="facts", description="Pulls a random quote in the internet")
    @commands.guild_only()
    async def get_facts(self, ctx: commands.Context) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://asli-fun-fact-api.herokuapp.com/') as r:
                result = await r.json()
                fact = result['data']['fact']
                if r.status in {200, 201}:
                    await ctx.send(f"Here's a random fact: {fact}")
                else:
                    await ctx.send("`Unable to process command. Please try again.`")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Basics(bot))
