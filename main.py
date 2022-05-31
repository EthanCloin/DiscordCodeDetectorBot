import discord
import os
from dotenv import load_dotenv
from guesslang import Guess
import subprocess
import logging

logging.basicConfig(filename="logs/bot_actions.log", filemode="a", level="DEBUG")
_log = logging.getLogger(__name__)

if __name__ == '__main__':
    subprocess.run("python3 code_guessing.py")
