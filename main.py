import discord
import os
from dotenv import load_dotenv
from guesslang import Guess


# load_dotenv()
# TOKEN = os.getenv("DISCORD_TOKEN")
# print(TOKEN)
# client = discord.Client()


# @client.event
# async def on_ready():
#     print(f"{client.user} has connected to Discord!")


# def parseCode(message):
#
#     print("")


# @client.event
# async def on_message(message):
#     parseCode(message)


def guess_test(code_string: str):
    guess = Guess()
    return guess.language_name(code_string)


if __name__ == '__main__':
    # client.run(TOKEN)
    test_result = guess_test("""
    print("Hello World!") 
    """)
    print(test_result)
