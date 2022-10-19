import discord
from discord.ext import commands

class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print("Mods Cog: Loaded!")

    # Ban someome
    @commands.hybrid_command(name='ban')
    @commands.has_guild_permissions(ban_members=True)
    async def do_ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason = reason)
        except:
            print(f'Unable to ban {member}.')
        else:
            await ctx.send(f"{member} was banned for {reason}")

    # Unban someone
    @commands.hybrid_command(name='unban')
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

    # Kick someone
    @commands.hybrid_command(name='kick')
    @commands.has_guild_permissions(ban_members=True)
    async def do_kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason = reason)
        except:
            print(f'Unable to kick {member}.')
        else:
            await ctx.send(f'{member} kicked for {reason}')

    # Get ban list
    @commands.hybrid_command(name='getbans')
    @commands.has_guild_permissions(ban_members=True)
    async def do_getbans(self, ctx):
        bannedId = await ctx.guild.bans()
        print(bannedId)

async def setup(bot):
    await bot.add_cog(Mods(bot))
