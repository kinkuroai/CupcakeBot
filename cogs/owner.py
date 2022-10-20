import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print("Owner Cog: Loaded!")

    # Channel Purge
    @commands.command(name='purge', hidden=True)
    @commands.is_owner()
    async def do_purge(self, ctx):
        try:
            await ctx.channel.purge()
        except:
            chanid = ctx.message.channel.id
            channame = ctx.message.channel.name
            print(f'Unable to purge: #{channame} - ID:{chanid}')
        else:
            chanid = ctx.message.channel.id
            channame = ctx.message.channel.name
            print(f'Successfully purged: #{channame}(ID:{chanid})')
    
    # Get Channel ID and name
    @commands.command(name='getchaninfo', hidden=True)
    @commands.is_owner()
    async def do_getchaninfo(self, ctx: commands.Bot) -> None:
        try:
            chanid = ctx.message.channel.id
            channame = ctx.message.channel.name
            await ctx.author.send(f"Channel ID: {chanid} - Channel Name: {channame}")
        except:
            print("Unable to process command.")
            
    # Load extension
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def do_load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`LOADED EXTENSION!`**')

    # Unload extension
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def do_unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`UNLOADED EXTENSION!`**')

    # Reload extension
    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def do_reload(self, ctx, *, cog: str):
        try:
            self.bot.reload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'**`RELOADED EXTENSION!`**')

async def setup(bot):
    await bot.add_cog(Owner(bot))
