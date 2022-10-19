import discord
from discord.ext import commands

class RoleManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print("RoleManager Cog: Loaded!")

    # Autorole | TO ADD: Custom roles, etc
    @commands.Cog.listener()
    async def on_member_join(self, member):
        give_role = discord.utils.get(member.guild.roles, name='Crew')
        try:
            await member.add_roles(give_role)
            print('Success')
        except:
            print('Failed to do anything.')

    # Make the bot create vanity roles
    @commands.command(name='crole')
    @commands.has_guild_permissions(manage_roles=True)
    async def do_crole(self, ctx, role):
        check_role = discord.utils.get(ctx.guild.roles, name=role)
        if not check_role:
            await ctx.author.send('Role not found. Creating role.')
            try:
                new_role = await ctx.guild.create_role(name=role, hoist=True)
            except discord.Forbidden as e:
                raise e
            else:
                await ctx.author.send(f'{role} was created.')
        else:
            await ctx.author.send(f'{role} already exists!')

    # Give role to users
    @commands.command(name='addrole')
    @commands.has_guild_permissions(manage_roles=True)
    async def do_addroles(self, ctx, member: discord.Member=None, *role):
        role = discord.utils.get(ctx.guild.roles, name=' '.join(role))
        try:
            await member.add_roles(role)
        except discord.Forbidden as e:
            raise e
        else:
            await ctx.send(f'{member.display_name} has **`{role.name}`** as a new role!')

    # Remove user role
    @commands.command(name='remrole')
    @commands.has_guild_permissions(manage_roles=True)
    async def do_remroles(self, ctx, member: discord.Member=None, *role):
        role = discord.utils.get(ctx.guild.roles, name=' '.join(role))
        try:
            await member.remove_roles(role)
        except discord.Forbidden as e:
            raise e
        else:
            await ctx.send(f'{member.display_name} is removed from **`{role.name}`** role.')

    # Delete a role
    @commands.command(name='drole')
    @commands.has_guild_permissions(manage_roles=True)
    async def do_drole(self, ctx, role):
        target_role = discord.utils.get(ctx.guild.roles, name=role)
        if target_role:
            try:
                await target_role.delete()
                await ctx.send(f'Role `{role}` deleted.')
            except:
                await ctx.send('Something went wrong.')
        else:
            await ctx.send('Role not found.')

async def setup(bot):
    await bot.add_cog(RoleManager(bot))
