import discord
from discord.ext import commands
from discord import app_commands

class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    async def cog_load(self):
        print("Owner Cog: Loaded!")

    # Channel Purge
    @commands.command(name='purge', hidden=True)
    @commands.is_owner()
    async def do_purge(self, ctx: commands.Context) -> None:
        try:
            await ctx.channel.purge()
        except:
            chanid = ctx.message.channel.id
            channame = ctx.message.channel.name
            print(f'Unable to purge: #{channame}(ID:{chanid})')
        else:
            chanid = ctx.message.channel.id
            channame = ctx.message.channel.name
            print(f'Successfully purged: #{channame}(ID:{chanid})')
    
    # Sync Commands
    @commands.command(name='syncnow', hidden=True)
    @commands.is_owner()
    async def do_syncnow(self, ctx: commands.Context) -> None:
        '''
        Temporary sync command. Works but I feel like there's a better way to do it.
        '''
        try:
            print(discord.Object(0))
            await self.bot.tree.sync()
        except:
            print("Something went wrong!!")
        else:
            print("Successfully synced")
    
    # Get Channel ID and name
    @commands.command(name='getchaninfo', hidden=True)
    @commands.is_owner()
    async def do_getchaninfo(self, ctx: commands.Context) -> None:
        try:
            chanid = ctx.message.channel.id
            channame = ctx.message.channel.name
            await ctx.author.send(f"Channel ID: {chanid} - Channel Name: {channame}")
        except:
            print("Unable to process command.")
            
    # Load extension
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def do_load(self, ctx: commands.Context, cog: str) -> None:
        try:
            await self.bot.load_extension("{}".format(cog))
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'**`LOADED EXTENSION {cog}!`**')

    # Unload extension
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def do_unload(self, ctx: commands.Context, cog: str) -> None:
        try:
            await self.bot.unload_extension("{}".format(cog))
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'**`UNLOADED EXTENSION {cog}!`**')

    # Reload extension
    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def do_reload(self, ctx: commands.Context, cog: str) -> None:
        try:
            await self.bot.reload_extension("{}".format(cog))
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'**`RELOADED EXTENSION {cog}!`**')

async def setup(bot: commands.Bot):
    await bot.add_cog(Owner(bot))
