import aiosqlite
import discord
from discord.ext import commands

"""
DB STUFF HERE
"""

class CupcakeDB(commands.Cog):
    """"""
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
    
    async def cog_load(self):
        print("CupcakeDB Cog: Loaded")
    
    # DB parent group
    @commands.group()
    async def db(self, ctx: commands.Context) -> None:
        if ctx.invoked_subcommand is None:
            await ctx.send("`Invalid db command passed..`")
    
    # Connect to database and create required tables if they do not exist
    @db.command("create")
    @commands.is_owner()
    async def do_createdb(self, ctx: commands.Context) -> None:
        conn = await aiosqlite.connect("bot.db")
        await conn.execute("CREATE TABLE IF NOT EXISTS USERS (USER_ID INT, DISPLAY_NAME VARCHAR(255), USER_DISCRIMINATOR INT, WARNS INT, COINS INT)")
        await conn.execute('CREATE TABLE IF NOT EXISTS BANS (USER_ID INT, DISPLAY_NAME VARCHAR(255), USER_DISCRIMINATOR INT)')
        await conn.commit()
        await conn.close()
        print("DB successfully created.")
    
    @db.command("destroy")
    @commands.is_owner()
    async def do_destroydb(self, ctz: commands.Context) -> None:
        pass
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CupcakeDB(bot))