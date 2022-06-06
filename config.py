"""dataclass with attributes to dictate behavior of code_detector_bot
and logs"""

import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


def get_ignored_languages() -> list:
    return ["Batchfile", "INI"]


def get_trigger_emojis() -> list:
    return ["👨‍💻", ":m:", "🥳"]


@dataclass
class Config:
    dm_user: bool = True
    msg_channel: bool = False
    trigger_on_reaction: bool = True
    trigger_on_message: bool = False
    default_msg: str = (
        "Looks like you are trying to send a block of {{LANGUAGE}} code here!\n"
        "Try using Discord's built-in code-block element instead.\n"
        "eg: \`\`\`python\nprint('Hello World!')\n\`\`\`"
        "\n```python\nprint('Hello World!')```"
    )
    default_msg_programming_language: str = "{{LANGUAGE}}"
    ignored_languages: list = field(default_factory=get_ignored_languages)
    trigger_emojis: list = field(default_factory=get_trigger_emojis)


# -- Logging -- #
ERROR_LOG_FILENAME = os.getenv("ERROR_LOG_FILENAME")
DEBUG_LOG_FILENAME = os.getenv("DEBUG_LOG_FILENAME")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s:%(name)s:%(process)d:%(lineno)d "
            "%(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(message)s",
        },
    },
}
