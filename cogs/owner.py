import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner Cog: LOADED!')
    
    # Get Channel ID
    @commands.command(name='getchid', hidden=True)
    @commands.is_owner()
    async def do_getchid(self, ctx, *, given_name=None):
        channel = discord.utils.get(ctx.guild.channels, name=given_name)
        channel_id = channel.id
        text_channel = self.bot.get_channel(channel_id)
        await ctx.send("Sending ID through DM..")
        await ctx.author.send(text_channel.mention + " ID is " + str(channel_id))

    # Channel Purge
    @commands.command(name='purge', aliases=['mdel', 'chanerase'], hidden=True)
    @commands.is_owner()
    async def do_purge(self, ctx):
            await ctx.channel.purge()
            chanid = ctx.message.channel.id
            channame = ctx.message.channel.name
            print('Successfully purged: #{} - ID: {}'.format(channame, chanid))
    
    # Load extension
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def do_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    # Unload extension
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def do_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    # Reload extension
    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def do_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(f'**`SUCCESS: RELOADED EXTENSION SUCCESSFULLY!`**')

def setup(bot):
    bot.add_cog(Owner(bot))