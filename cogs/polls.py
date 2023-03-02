import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, question, option1, option2, option3=None, option4=None):
        # create embed
        embed = discord.Embed(title="It's Poll Time", description=question, color=discord.Color.blue())
        embed.add_field(name='Choice 1', value=option1, inline=True)
        embed.add_field(name='Choice 2', value=option2, inline=True)

        # add optional options
        if option3:
            embed.add_field(name='Choice 3', value=option3, inline=True)
        if option4:
            embed.add_field(name='Choice 4', value=option4, inline=True)

        # send embed
        message = await ctx.send(embed=embed)

        # add reactions
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')
        if option3:
            await message.add_reaction('👌')
        if option4:
            await message.add_reaction('💩')

async def setup(bot):
    await bot.add_cog(Poll(bot))
