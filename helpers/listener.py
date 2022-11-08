import discord
import aiohttp
import os
import utils
import logging
from discord.ext import commands

logger = logging.getLogger('discord_info.log')

class CakeListener(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print("CakeListener Cog: Loaded!")

    # Autorole | TO ADD: Custom roles, etc
    @commands.Cog.listener()
    async def on_member_join(self, member):

        give_role = discord.utils.get(member.guild.roles, name=utils.AUTOROLE_NAME)
        channel = discord.utils.get(member.guild.channels, name=utils.WELCOME_CHANNEL)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.best/api/v2/wave') as r:
                    result = await r.json()
                    hello_image = result['results'][0]['url']
                    embed = discord.Embed(title="Hello there!", description=f"Welcome to the server, {member.mention}!")
                    embed.set_image(url=hello_image)
                    await channel.send(embed=embed)
                    await member.add_roles(give_role)
                    logger.info(f"`{member} joined the server and was given the {give_role} role.`")
                    
        except:
            print('Failed to do anything.')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CakeListener(bot))
