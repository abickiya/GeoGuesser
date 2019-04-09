import discord

client = discord.Client()
SECRET = "KEY"


@client.event
async def on_ready():
    print('Logged on as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!play"):
        await message.channel.send("Starting Game!")

client.run(SECRET)
