import discord

client = discord.Client()

global botPrefix


@client.event
async def on_ready():
    print("Logged in as: " + client.user.name)
    print(client.user.name + " is now logged in!")
    botPrefix = ">"
    print("Bot prefix is set to: " + botPrefix)

# Commands go here
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(botPrefix + "hello"):
        await message.channel.send("Cupcake Bot is running, Master Mavz.")

client.run('ODY3Mjg5Mjk0NzAzMjk2NTEy.YPe8GQ.dnCTcelm4sB-HvxO521GcoZEj4c')