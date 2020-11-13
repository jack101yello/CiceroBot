import discord
from handler import *
client = discord.Client()
TOKEN = ""

@client.event
async def on_ready(): # Runs when the Bot first connects
    print('Diagnostics:')
    print('Connected as {0.user}'.format(client))  # Username
    print('Joining the following guilds:', end=""), print(await client.fetch_guilds(limit=150).flatten())
    print('Connection obtained via:', end=""), print(client.ws)
    print('Application information:', end=""), print(await client.application_info())
    print('Log:')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!cicero.lat'):
        response = get_response_lat(message.content[11:])
        print('/// New command')
        print('Command: ', end=""), print(message.content)
        print('User: ', end=""), print(message.author)
        print('Response: ', end=""), print(response)
        await message.channel.send(response) # Sends message
    elif message.content.startswith('!cicero'):
        response = get_response(message.content[7:])
        print('/// New command')
        print('Command: ', end=""), print(message.content)
        print('User: ', end=""), print(message.author)
        print('Response: ', end=""), print(response)
        await message.channel.send(response)  # Sends message

# Commends to run the Bot itself
client.run(TOKEN)
client.login(TOKEN)