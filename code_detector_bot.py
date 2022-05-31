import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from guesslang import Guess

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(TOKEN)
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

# react to event for when user sends message

@client.event
async def on_message(message):
    guess = Guess()
    if guess.language_name(message) != "Batchfile":
        # send popup message to user suggesting a block comment
        await message.channel.send("Stop it get some help, format your code lol")
    
    


# send popup message to user suggesting a block comment
@bot.command(name="my_cmd")
async def command_testing(ctx):
    response = "you have commanded, i have complied"
    await ctx.send(response)


def suggest_language_formatted():
    pass


# automatically delete and reformat user message


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
