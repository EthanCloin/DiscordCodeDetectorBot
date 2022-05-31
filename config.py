from dataclasses import dataclass, field


def get_ignored_languages() -> list:
    return ["Batchfile", "INI"]


def get_trigger_emojis() -> list:
    return ["👨‍💻"]


@dataclass(init=False)
class Config:
    dm_user: bool = True
    msg_channel: bool = False
    trigger_on_reaction: bool = True
    trigger_on_message: bool = False
    default_msg: str = (
        "Looks like you are trying to send a block of {{LANGUAGE}} code here!"
        "Try using Discord's built-in code-block element instead.\n"
        "eg: ```python\nprint('Hello World!')\n```"
    )
    default_msg_programming_language: str = "{{LANGUAGE}}"
    ignored_languages: list = field(default_factory=get_ignored_languages)
    trigger_emojis: list = field(default_factory=get_trigger_emojis)
