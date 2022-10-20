import discord
import os
import requests
import aiohttp
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
BOT_ZONE = os.getenv('BOT_ZONE')

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

    @commands.hybrid_command(name="waifu")
    async def get_waifu(self, ctx: commands.Context, a: str) -> None:
        async with aiohttp.ClientSession() as session:
            if a == 'nsfw':
                async with session.get('https://api.waifu.im/random/?selected_tags=hentai') as r:
                    result = await r.json()
                    waifu_image = result['images'][0]['url']
                    if r.status in {200, 201}:
                        print(waifu_image)
                        await ctx.send(waifu_image)
                    else:
                        print("`Unable to process command. Please try again.`")
            elif a == 'sfw':
                async with session.get('https://api.waifu.im/random/?selected_tags=waifu') as r:
                    result = await r.json()
                    waifu_image = result['images'][0]['url']
                    if r.status in {200, 201}:
                        print(waifu_image)
                        await ctx.send(waifu_image)
                    else:
                        print("`Unable to process command. Please try again.`")

    @commands.hybrid_command(name="facts")
    async def get_facts(self, ctx: commands.Context) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://asli-fun-fact-api.herokuapp.com/') as r:
                result = await r.json()
                fact = result['data']['fact']
                await ctx.send(f"Here's a random fact: {fact}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Basics(bot))
