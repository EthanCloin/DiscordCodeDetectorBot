import discord
import os
from dotenv import load_dotenv
import logging
from code_detector_bot import CodeDetector
from config import Config

# logging.basicConfig(filename="logs/bot_actions.log", filemode="a", level="DEBUG")
# _log = logging.getLogger(__name__)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CONFIG = Config()


if __name__ == "__main__":
    client = CodeDetector(DISCORD_TOKEN, CONFIG)
    client.run()
