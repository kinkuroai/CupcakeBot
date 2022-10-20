import discord
import requests
from discord.ext import commands

# Still under construction lmao

class AnimeSearch(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print('AnimeSearch Cog: Loaded!')

    @commands.hybrid_command(name='anime')
    async def do_anisearch(self, ctx: commands.Context, *, search: str) -> None:
        try:
            r = requests.get(f'https://api.jikan.moe/v4/anime/?q={search}')
            result = r.json()

            title_english = result['data'][0]['title_english']
            title_japanese = result['data'][0]['title_japanese']
            synopsis = result['data'][0]['synopsis']
            image = result['data'][0]['images']['jpg']['image_url']
            score = result['data'][0]['score']
            episodes = result['data'][0]['episodes']
            status = result['data'][0]['status']

        except:
            print("Something went wrong.")

        else:
            #print(title_english)
            #print(status)

            embed = discord.Embed(title=f"{title_english} - {title_japanese}", description=f"{synopsis}")
            embed.set_image(url=image)
            embed.add_field(name="Score", value=score, inline=True)
            embed.add_field(name="Episodes", value=episodes, inline=True)
            embed.add_field(name="Status", value=status, inline=True)

            await ctx.send(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AnimeSearch(bot))
