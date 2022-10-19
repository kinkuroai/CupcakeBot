import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print("Owner Cog: Loaded!")

    # Get Channel ID
    @commands.command(name='getchid', aliases=['cid'], hidden=True)
    @commands.is_owner()
    async def do_getchid(self, ctx, *, given_name=None):
        try:
            channel = discord.utils.get(ctx.guild.channels, name=given_name)
            channel_id = channel.id
            text_channel = self.bot.get_channel(channel_id)
        except:
            print('Unable to get CHANNEL ID.')
        else:
            await ctx.author.send(text_channel.mention + " ID is " + str(channel_id))

    # Channel Purge
    @commands.command(name='purge', aliases=['clear'], hidden=True)
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
                print(f'Successfully purged: #{channame} - ID:{chanid}')

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
