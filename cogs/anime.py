import discord
import aiohttp, os
import logging
from discord.ext import commands

# Still under construction lmao

logger = logging.getLogger('discord_info.log')

class AnimeSearch(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print('AnimeSearch Cog: Loaded!')
    
    # Searches MAL for the anime
    @commands.hybrid_command(name='anime', description="Searches for anime in MAL")
    @commands.guild_only()
    async def do_anisearch(self, ctx: commands.Context, *, search: str) -> None:
        try:
            async with aiohttp.ClientSession() as session:

                async with session.get(f'https://api.jikan.moe/v4/anime/?q={search}') as r:
                    result = await r.json()
                    
                    data = result['data'][0]

                    title_english = data['title_english']
                    title_japanese = data['title_japanese']
                    synopsis = data['synopsis']
                    image = data['images']['jpg']['image_url']
                    score = data['score']
                    episodes = data['episodes']
                    status = data['status']

                    embed = discord.Embed(title=f"{title_english} - {title_japanese}", description=f"{synopsis}", colour=0x236DC9)
                    embed.set_image(url=image)
                    embed.add_field(name="Score", value=score, inline=True)
                    embed.add_field(name="Episodes", value=episodes, inline=True)
                    embed.add_field(name="Status", value=status, inline=True)

                    await ctx.send(embed=embed)

        except:
            logger.error("`**SOMETHING WENT WRONG WITH THE ANIME COG**`")

    # Gets an anime quote for you
    @commands.hybrid_command(name="aniquote", description="Pulls an anime quote for you")
    @commands.guild_only()
    async def get_quote(self, ctx: commands.Context, *, name=None) -> None:
        async with aiohttp.ClientSession() as session:

            # Pull a random quote if no name is specified
            if name is None:
                async with session.get(f'https://animechan.vercel.app/api/random') as r:
                    result = await r.json()
                    title = result['anime']
                    character = result['character']
                    quotes = result['quote']
                    await ctx.send(f"**{character} ({title})**: '{quotes}'")
                    
            else:   
                # Get random quote of the character
                # Still kinda wonky
                async with session.get(f'https://animechan.vercel.app/api/random/character?name={name}') as r:
                    result = await r.json()
                    title = result['anime']
                    character = result['character']
                    quotes = result['quote']
                    await ctx.send(f"**{character} ({title})**: '{quotes}'")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AnimeSearch(bot))
