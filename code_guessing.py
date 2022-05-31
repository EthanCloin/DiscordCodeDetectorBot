from guesslang import Guess

import discord
import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


# react to event for when user sends message
@client.event
async def on_message(message):
    guess = Guess()
    if guess.language_name(message.content) != "Batchfile":
        # send popup message to user suggesting a block comment
        await message.channel.send("Stop it get some help, format your code lol")


# automatically delete and reformat user message
if __name__ == "__main__":
    pass


client.run(TOKEN)
