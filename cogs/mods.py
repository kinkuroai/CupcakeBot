import discord
from discord.ext import commands

class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mods Cog: LOADED!')
    
    # Ban someome
    @commands.command(name='ban')
    @commands.has_guild_permissions(ban_members=True)
    async def do_ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason = reason)
        await ctx.send(f"{member} was banned for {reason}")

    # Unban someone
    @commands.command(name='unban')
    @commands.has_guild_permissions(ban_members=True)
    async def do_unban(self, ctx, *, member):        
        if "#" in ctx.message.content:
            banned_users = await ctx.guild.bans()
            for ban_entry in banned_users: 
                member_name, member_discriminator = member.split('#')
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
        else:
            member = await self.bot.fetch_user(int(member))
            await ctx.guild.unban(member)

    # Get ban list
    @commands.command(name='getbans')
    @commands.has_guild_permissions(ban_members=True)
    async def do_getbans(self, ctx):
        bannedId = await ctx.guild.bans()
        print(bannedId)

def setup(bot):
    bot.add_cog(Mods(bot))