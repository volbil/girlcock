from aiogram import Dispatcher
from app.utils import get_bot
import asyncio
import logging


logging.basicConfig(level=logging.INFO)


async def main():
    logging.info("Starting bot...")

    from app.general import router as general_router

    bot = get_bot()

    dispatcher = Dispatcher()

    dispatcher.include_router(general_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
