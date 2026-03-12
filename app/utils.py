from functools import lru_cache
from aiogram import Bot
import tomllib
import re


@lru_cache()
def get_settings(base_name="default"):
    with open("settings.toml", "rb") as file:
        return tomllib.load(file)[base_name]


def get_bot():
    settings = get_settings()
    return Bot(token=settings["bot"]["token"])


def find_twitter_links(text: str) -> list[str]:
    pattern = r'(?:https?://)?(?:www\.)?\b(?:x\.com|twitter\.com)/[^\s<>"\']*'
    matches = re.findall(pattern, text)
    return [m if m.startswith("http") else f"https://{m}" for m in matches]
