# import python discord library
import discord

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.DEBUG)

# if this doesn't work, try "all" instead of "default"
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# create a client object with keyword-only argument "intents"
# intents is a bit like permissions for the bot
# we need to specify that we want to receive messages
# and that we want to send messages
# client = discord.Client(intents=discord.Intents(messages=True, guilds=True))
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

# run the bot
# load the token from a file called token.txt
with open('token.txt', 'r') as f:
    token = f.read()
client.run(token)
# ```

# ## Running the bot
# To run the bot, you can use the command `python gettingstarted.py` in the terminal. If you are using a virtual environment, make sure you activate it first.

# ## Adding the bot to a server
# To add the bot to a server, you need to create an invite link. You can do this by going to the [Discord Developer Portal](https://discord.com/developers/applications) and selecting your application. Then, go to the OAuth2 tab and select the bot scope. You can then select the permissions you want the bot to have. Once you have done this, you can copy the link and paste it into your browser. You will then be able to add the bot to a server.

# ## Resources
# - [Discord Developer Portal](https://discord.com/developers/applications)
# - [Discord.py Documentation](https://discordpy.readthedocs.io/en/latest/index.html)
# - [Discord.py API Reference](https://discordpy.readthedocs.io/en/latest/api.html)
# - [Discord.py Discord Server](https://discord.gg/r3sSKJJ)
# - [Discord.py FAQ](https://discordpy.readthedocs.io/en/latest/faq.html)
# - [Discord.py Wiki](https://discordpy.readthedocs.io/en/latest/index.html)

# ## License
# This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
