import discord
from discord.ext import commands

class SyncThing(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    async def cog_load(self):
        print('Sync Cog: Loaded')
    
    """
    Still figuring out how to implement command syncing properly.
    Gomen!
    """
    
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SyncThing(bot))
