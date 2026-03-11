from app.utils import find_twitter_links
from aiogram.filters import Command
from aiogram.types import Message
from urllib.parse import urlsplit
from aiogram import Router


router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.reply(
        "Вас втомили огидненькі посилання з твітера без попереднього перегляду?\n\n"
        "Я допоможу!\n\nВід @lipsum_blog"
    )


@router.message()
async def fix_links(message: Message) -> None:
    if not message.text:
        return

    links = find_twitter_links(message.text)

    if not links:
        return

    for link in links:
        url = urlsplit(link)

        if url.netloc not in ["x.com", "twitter.com"]:
            continue

        if not url.path:
            continue

        fixed_url = "https://girlcockx.com" + url.path

        await message.reply(fixed_url)

        break
