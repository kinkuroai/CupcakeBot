import discord
from discord.ext import commands
from discord import app_commands
from mal import *
import requests

class Basics(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print('Basics Cog: Loaded!')

    # Make the bot say something
    @commands.hybrid_command(name='say', aliases=['repeat', 'again'])
    async def do_say(self, ctx: commands.Context, *, msg: str) -> None:
        await ctx.send(msg)
        await ctx.message.delete()

    # Search anime on MAL
    @commands.hybrid_command(name='anime', aliases=['animu', 'ani'])
    async def do_anime(self, ctx: commands.Context, *, title: str) -> None:
        search = AnimeSearch(title)
        anires = search.results[0].mal_id
        anime = Anime(anires)
        emb = discord.Embed(title='{} - {}'.format(anime.title, anime.title_japanese), description=anime.synopsis, color=0x00ff00)
        emb.set_image(url=anime.image_url)
        emb.add_field(name="Score", value=anime.score, inline=True)
        emb.add_field(name="Episodes", value=anime.episodes, inline=True)
        emb.add_field(name="Status", value=anime.status, inline=True)
        emb.set_footer(text="via MAL - {}".format(anime.url), icon_url=anime.image_url)
        channel = self.bot.get_channel(948589194454904894)
        await channel.send(embed=emb)

    # Search manga on MAL
    @commands.hybrid_command(name='manga', aliases=['mango', 'man'])
    async def do_manga(self, ctx: commands.Context, *, title: str):
        search = MangaSearch(title)
        manres = search.results[0].mal_id
        manga = Manga(manres)
        emb = discord.Embed(title='{} - {}'.format(manga.title, manga.title_japanese), description=manga.synopsis, color=0x00ff00)
        emb.set_image(url=manga.image_url)
        emb.add_field(name="Score", value=manga.score, inline=True)
        emb.add_field(name="Volumes", value=manga.volumes, inline=True)
        emb.add_field(name="Status", value=manga.status, inline=True)
        emb.set_footer(text="via MAL - {}".format(manga.url), icon_url=manga.image_url)
        channel = self.bot.get_channel(948589194454904894)
        await channel.send(embed=emb)

    @commands.hybrid_command(name="waifu")
    async def get_waifu(self, ctx: commands.Context, taipu: str) -> None:
        try:
            if taipu == "nsfw":
                r = requests.get("https://api.waifu.pics/nsfw/waifu")
            elif taipu == "sfw":
                r = requests.get("https://api.waifu.pics/sfw/waifu")
            else:
                await ctx.send("**`INVALID TYPE: Enter sfw or nsfw`**")
                await ctx.send("**`EXAMPLE: ?waifu sfw`**")
        except:
            print("Something went wrong.")
        else:
            result = r.json()
            await ctx.send(result['url'])

    @commands.hybrid_command(name="facts")
    async def get_excuse(self, ctx: commands.Context) -> None:
        try:
            r = requests.get("https://asli-fun-fact-api.herokuapp.com/")
        except:
            print("Something went wrong.")
        else:
            result = r.json()
            print(result['data']['fact'])
            await ctx.send("Here's a random fact:" + " " + result['data']['fact'])

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Basics(bot))
