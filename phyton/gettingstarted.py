# import python discord library
from ast import List
import discord
from discord.ext import commands
import random

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.DEBUG)

# if this doesn't work, try "all" instead of "default"
intents = discord.Intents.default()
# intents=discord.Intents(messages=True, guilds=True)
client = discord.Client(intents=intents)
# client = discord.Client()

# event handler for when the bot is ready
@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))	

# event handler for when a message is sent
@client.event
async def on_message(message):
    # print message content to the console
    print(message)
    print(message.author)
    print(message.author.bot)
    print(client.user)
    print(message.content)
    # ignore messages sent by the bot
    if message.author == client.user:
        return

    logging.debug("message received")
    # send chat message to the channel
    await message.channel.send('Hello!')
    # await message.channel.send(message.content[::-1])

    # check if the message contains the word "hello"
    if message.content.startswith('hello'):
        # send a message to the channel
        await message.channel.send('Hello!')

# set app_commands ping, respond with pong
@discord.app_commands.command(name='ping', description='Respond with pong', nsfw=False)
async def ping(ctx):
    await ctx.send('pong')

app_commands = discord.app_commands
@app_commands.command()
async def fruits(interaction: discord.Interaction, fruit: str):
    await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')

@fruits.autocomplete('fruit')
async def fruits_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
    return [
        app_commands.Choice(name=fruit, value=fruit)
        for fruit in fruits if current.lower() in fruit.lower()
    ]

# load the token from a file called token.txt
with open('token.txt', 'r') as f:
    token = f.read()

# run the bot
client.run(token)
