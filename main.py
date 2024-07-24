import discord
from discord.ext import commands

client = commands.Bot(command_prefix='j.', intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "the carrots singing him a song! 🥕✨"))
    print("Jack is up and running!") # testing in terminal

@client.command()
async def jackTest(ctx):
    await ctx.send("Hi, I'm Jack!") # testing in channel

@client.event
async def on_message(message):
    if message.channel.id == VERIFICATION_CHANNEL_ID and message.content == "Sprouted":
        await message.delete()
        role = message.guild.get_role(ROLE_ID)
        welcome_channel = client.get_channel(WELCOME_CHANNEL_ID)
        if role in message.author.roles:
            return
        if role:
            await message.author.add_roles(role)
            if welcome_channel:
                await welcome_channel.send(f'{message.author.mention}, welcome in!')
            else:
                await message.channel.send(f'Error sending welcome message :()')
        else:
            await message.channel.send(f'Error giving role :()')
    await client.process_commands(message)

client.run(BOT_TOKEN)
