"""original design as we were learning. the functions here are now present
in code_detector_bot.py as class methods."""

from guesslang import Guess

import discord
import os
from dotenv import load_dotenv


# setup
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


# listeners
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    guess = Guess()
    if guess.language_name(message.content) != "Batchfile":
        # send popup message to user suggesting a block comment
        await message.channel.send("Stop it get some help, format your code lol")


@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    emoji = reaction.emoji
    if user.bot:
        return

    if emoji == "👨‍💻":
        guess = Guess()
        programming_lang = guess.language_name(message.content)

        if programming_lang != "Batchfile" and programming_lang != "INI":
            # send popup message to user suggesting a block comment
            await message.channel.send("Stop it get some help, format your code lol")
        return

    else:
        return


# automatically delete and reformat user message

if __name__ == "__main__":
    pass


client.run(TOKEN)
