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

@client.event
async def on_reaction_add(reaction, user):
    embed = reaction.embeds[0]
    emoji = reaction.emoji

    if user.bot:
        return

    if emoji == "emoji 1":
        # fixed_channel = client.get_channel(channel_id)
        # await fixed_channel.send(embed=embed)
    elif emoji == "emoji 2":
        #do stuff
    elif emoji == "emoji 3":
        #do stuff
    else:
        return
# automatically delete and reformat user message
if __name__ == "__main__":
    pass


client.run(TOKEN)
