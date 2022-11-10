import discord
import logging
import utils
from discord.ext import commands

"""
Going to rewrite the mod commands since most of them, discord does a lot better.
"""

logger = logging.getLogger('discord_info.log')

class Mods(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    async def cog_load(self):
        print("Mods Cog: Loaded!")
    
    # Add role
    @commands.command(name='addrole')
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def do_addrole(self, ctx: commands.Context, member: discord.Member, *role) -> None:
        role = discord.utils.get(ctx.guild.roles, name=" ".join(role))
        try:
            await member.add_roles(role)
        except:
            logger.error(f"`Unable to add role to {memeber.display_name}`")
        else:
            await utils.send_embed(ctx, "ROLE ADDED!", f"Added {role.mention} role to {member.mention}")
    
    # Remove Role
    @commands.command(name="remrole")
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def do_remrole(self, ctx: commands.Context, member: discord.Member, *role) -> None:
        role = discord.utils.get(ctx.guild.roles, name=" ".join(role))
        try:
            await member.remove_roles(role)
        except:
            logger.error(f"`Unable to remove role from {member.display_name}`")
        else:
            await utils.send_embed(ctx, "ROLE REMOVED!", f"Removed {role.mention} from {member.mention}")

    # Kick someone
    @commands.command(name='kick')
    @commands.has_guild_permissions(ban_members=True)
    @commands.guild_only()
    async def do_kick(self, ctx: commands.Context, member: discord.Member, *, reason=None) -> None:
        try:
            embed = discord.Embed(title="Kicked off the server!", description="Low-level Punishment", colour=0xea213a)
            embed.add_field(name="Name:", value=f"{member.display_name}", inline=True)
            embed.add_field(name="Reason:", value=f"{reason}", inline=True)
            embed.set_thumbnail(url=member.display_avatar)
            await ctx.send(embed=embed)
            await member.kick(reason = reason)
        except:
            await ctx.author.send(f'Unable to kick {member.display_name}.')
    
    # Warns someone
    @commands.command(name='warn')
    @commands.has_guild_permissions(ban_members=True)
    @commands.guild_only()
    async def do_warn(self, ctx: commands.Context, member: discord.Member, *, reason=None) -> None:
        pass

    # Mutes someone
    @commands.command(name='mute')
    @commands.has_guild_permissions(ban_members=True)
    @commands.guild_only()
    async def do_mute(self, ctx: commands.Context, member: discord.Member, *, reason=None) -> None:
        pass

    # Bans someone
    @commands.command(name='ban')
    @commands.has_guild_permissions(ban_members=True)
    @commands.guild_only()
    async def do_ban(self, ctx: commands.Context, member: discord.Member, *, reason=None) -> None:
        pass
    
    # Unbans someone
    @commands.command(name='unban')
    @commands.has_guild_permissions(ban_members=True)
    @commands.guild_only()
    async def do_unban(self, ctx: commands.Context, member: str, discriminator: int) -> None:
        pass

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Mods(bot))
