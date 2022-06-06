"""extension of the discord.Client class with custom behavior to detect what programming
language a user has included in their message. can be configured in config.py to react
to specified emoji, or to all messages. potential features include dm-ing user, bot commands
to update the config information, or NLP to determine which sections of a message is code"""

import discord
from guesslang import Guess
from config import Config
import logging


_log = logging.getLogger(__name__)
# disabling imported logs
logging.getLogger("guesslang").disabled = True
logging.getLogger("discord").disabled = True


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

        if not self.config.trigger_on_message:
            _log.debug("msg ignored due to config")
            return

        guess = Guess()
        programming_language = guess.language_name(message.content)
        _log.debug(f"[msg] msg detected in language {programming_language}")

        if programming_language not in self.config.ignored_languages:
            # send popup message to user suggesting a block comment
            await message.channel.send(
                self.config.default_msg.replace(
                    self.config.default_msg_programming_language, programming_language
                )
            )
        _log.debug("[msg] msg ignored due to config ignored languages")
        return

    async def on_reaction_add(self, reaction, user):

        if not self.config.trigger_on_reaction:
            _log.debug("rxn ignored due to config")
            return
        if user.bot:
            _log.debug("rxn ignored due to bot src")
            return

        message = reaction.message
        emoji = reaction.emoji
        _log.debug(f"emoji detected: {emoji}")

        if emoji in self.config.trigger_emojis:
            guess = Guess()
            programming_language = guess.language_name(message.content)
            _log.debug(f"[rxn] msg detected in language {programming_language}")

            if programming_language not in self.config.ignored_languages:
                # send popup message to user suggesting a block comment
                await message.channel.send(
                    self.config.default_msg.replace(
                        self.config.default_msg_programming_language,
                        programming_language,
                    )
                )
        _log.debug("[rxn] msg ignored due to config ignored languages")
        return


if __name__ == "__main__":
    pass
