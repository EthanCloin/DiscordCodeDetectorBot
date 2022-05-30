import discord
import os
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

def parseCode(message):
    
    print("")



@client.event
async def on_message(message):
    parseCode(message)

client.run(TOKEN)