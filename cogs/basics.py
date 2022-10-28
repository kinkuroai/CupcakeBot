import discord
import aiohttp
import random
from discord.ext import commands

class Basics(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print('Basics Cog: Loaded!')

    # Make the bot say something
    @commands.hybrid_command(name='say')
    @commands.guild_only()
    async def do_say(self, ctx: commands.Context, *, msg: str) -> None:
        await ctx.send(msg)
        await ctx.message.delete()
    
    # Summons a random waifu
    @commands.hybrid_command(name="waifu")
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
    @commands.hybrid_command(name="facts")
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
