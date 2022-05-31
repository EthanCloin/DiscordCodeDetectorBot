import discord
from guesslang import Guess
from config import Config


class CodeDetector(discord.Client):
    """extension of dicord Client object with added code detector behavior"""

    def __init__(self, discord_token: str, config: Config, **options):
        super().__init__(**options)
        self.discord_token = discord_token
        self.config = config

    # listeners
    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

    async def on_message(self, message):
        guess = Guess()
        if guess.language_name(message.content) != "Batchfile":
            # send popup message to user suggesting a block comment
            await message.channel.send("Stop it get some help, format your code lol")

    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        emoji = reaction.emoji
        if user.bot:
            return

        if emoji == "👨‍💻":
            guess = Guess()
            programming_lang = guess.language_name(message.content)

            if programming_lang != "Batchfile" and programming_lang != "INI":
                # send popup message to user suggesting a block comment
                await message.channel.send(
                    "Stop it get some help, format your code lol"
                )
            return

        else:
            return


# @client.event
# async def on_ready():
#     print(f"{client.user} has connected to Discord!")
#
#
# # react to event for when user sends message
#
#
# @client.event
# async def on_message(message):
#     guess = Guess()
#     code = guess.language_name(message.content)
#     print(code)
#     if code != "Batchfile" and code != "INI":
#         # send popup message to user suggesting a block comment
#         await message.channel.send("Stop it get some help, format your code lol")
#
#
# # send popup message to user suggesting a block comment
# @bot.command(name="my_cmd")
# async def command_testing(ctx):
#     response = "you have commanded, i have complied"
#     await ctx.send(response)
#
#
# def suggest_language_formatted():
#     pass
#
#
# # automatically delete and reformat user message


if __name__ == "__main__":
    pass
