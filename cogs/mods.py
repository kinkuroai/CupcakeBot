import discord
from discord.ext import commands

"""
Going to rewrite the mod commands since most of them, discord does a lot better.
"""

class Mods(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_load(self):
        print("Mods Cog: Loaded!")

    # Kick someone
    @commands.command(name='kick')
    @commands.has_guild_permissions(ban_members=True)
    @commands.guild_only()
    async def do_kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            embed = discord.Embed(title="Kicked off the server!", description="Low-level Punishment", colour=0xea213a)
            embed.add_field(name="Name:", value=f"{member.display_name}", inline=True)
            embed.add_field(name="Reason:", value=f"{reason}", inline=True)
            embed.set_thumbnail(url=member.display_avatar)
            await ctx.send(embed=embed)
            await member.kick(reason = reason)
        except:
            await ctx.author.send(f'Unable to kick {member.display_name}.')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Mods(bot))
