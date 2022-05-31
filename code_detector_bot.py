import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from guesslang import Guess

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")

# react to event for when user sends message


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
