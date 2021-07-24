import discord
from discord.ext import commands
from mal import *

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Basics Cog: LOADED!')

    # Make the bot say something
    @commands.command(name='say', aliases=['repeat', 'again'])
    async def do_say(self, ctx, *, msg: str):
        await ctx.send(msg)
        await ctx.message.delete()
    
    # Search anime on MAL
    @commands.command(name='anime', aliases=['animu', 'ani'])
    async def do_anime(self, ctx, *, title):
        search = AnimeSearch(title)
        anires = search.results[0].mal_id
        anime = Anime(anires)
        emb = discord.Embed(title='{} - {}'.format(anime.title, anime.title_japanese), description=anime.synopsis, color=0x00ff00)
        emb.set_image(url=anime.image_url)
        emb.add_field(name="Score", value=anime.score, inline=True)
        emb.add_field(name="Episodes", value=anime.episodes, inline=True)
        emb.add_field(name="Status", value=anime.status, inline=True)
        emb.set_footer(text="via MAL - {}".format(anime.url), icon_url=anime.image_url)
        channel = self.bot.get_channel(865996369236066314)
        await channel.send(embed=emb)

    # Search manga on MAL
    @commands.command(name='manga', aliases=['mango', 'man'])
    async def do_manga(self, ctx, *, title):
        search = MangaSearch(title)
        manres = search.results[0].mal_id
        manga = Manga(manres)
        emb = discord.Embed(title='{} - {}'.format(manga.title, manga.title_japanese), description=manga.synopsis, color=0x00ff00)
        emb.set_image(url=manga.image_url)
        emb.add_field(name="Score", value=manga.score, inline=True)
        emb.add_field(name="Volumes", value=manga.volumes, inline=True)
        emb.add_field(name="Status", value=manga.status, inline=True)
        emb.set_footer(text="via MAL - {}".format(manga.url), icon_url=manga.image_url)
        channel = self.bot.get_channel(865996651906727977)
        await channel.send(embed=emb)

def setup(bot):
    bot.add_cog(Basics(bot))