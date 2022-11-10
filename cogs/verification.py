import discord
import aiosqlite
import utils
from discord.ext import commands

class CupcakeVerify(commands.Cog):
    """
    Server verification thing | Gonna convert to slash soon, having problems
    """
    def __init__(self, bot):
        self.bot: commands.Bot = bot
    
    async def cog_load(self):
        print("Verification Cog: Loaded")
    
    # Make sure you have ran ?db create when setting up the bot
    @commands.command(name="verify", description="Verifies your existence.")
    @commands.guild_only()
    async def do_checkdb(self, ctx: commands.Context) -> None:
        await ctx.message.delete()
        conn = await aiosqlite.connect("bot.db")
        cur = await conn.cursor()
        await cur.execute(f'SELECT * FROM USERS WHERE USER_ID="{ctx.author.id}";')
        is_exist = await cur.fetchone()
        if is_exist is None:
            #print("Checking..")
            await cur.execute(f'''INSERT INTO USERS (USER_ID, DISPLAY_NAME, USER_DISCRIMINATOR, WARNS, COINS)
            VALUES ("{ctx.author.id}", "{ctx.author.name}", "{ctx.author.discriminator}", "0", "0")''')
            await conn.commit()
            await utils.send_embed(ctx, "Congratulations!", f"You are now verified, {ctx.author.mention}")
        else:
            #print(is_exist[0])
            await utils.send_embed(ctx, "Hey there! ", f"You are already verified, {ctx.author.mention}!")
        await conn.close()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CupcakeVerify(bot))