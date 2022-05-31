from guesslang import Guess
import streamlit as st

import discord
import os
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(TOKEN)
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    st.success("Discord is up!")

# react to event for when user sends message

@client.event
async def on_message(message):
    guess = Guess()
    if guess.language_name(code_string) != "Batchfile":
        # send popup message to user suggesting a block comment
        await message.channel.send("Stop it get some help, format your code lol")
    
    
    





# automatically delete and reformat user message

def guess_test(code_string: str):
    guess = Guess()
    return guess.language_name(code_string)


if __name__ == "__main__":
    # client.run(TOKEN)
    pass

code = st.text_area("Code")
if st.button("TRY"):
    language = guess_test(code)
    st.success(language)

client.run(TOKEN)
