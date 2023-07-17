import asyncio
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from aiohttp import ClientSession
import config

API_ID = config.API_ID
API_HASH = config.API_HASH
SESSION1 = config.SESSION1
SESSION2 = config.SESSION2
SESSION3 = config.SESSION3
SESSION4 = config.SESSION4
SESSION5 = config.SESSION5
SESSION6 = config.SESSION6
SESSION7 = config.SESSION7
SESSION8 = config.SESSION8
SESSION9 = config.SESSION9


async def idle():
    while True:
        await asyncio.sleep(1)

async def main():
    aiosession = ClientSession()
    bots = []

    if SESSION1:
        bot1 = Client("bot1", api_id=API_ID, api_hash=API_HASH, session_string=SESSION1, plugins=dict(root="haku/modules"))
        bots.append(bot1)
    else:
        bots.append(None)

    if SESSION2:
        bot2 = Client("bot2", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2, plugins=dict(root="haku/modules"))
        bots.append(bot2)
    else:
        bots.append(None)

    if SESSION3:
        bot3 = Client("bot3", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3, plugins=dict(root="haku/modules"))
        bots.append(bot3)
    else:
        bots.append(None)

    if SESSION4:
        bot4 = Client("bot4", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4, plugins=dict(root="haku/modules"))
        bots.append(bot4)
    else:
        bots.append(None)

    if SESSION5:
        bot5 = Client("bot5", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5, plugins=dict(root="haku/modules"))
        bots.append(bot5)
    else:
        bots.append(None)

    if SESSION6:
        bot6 = Client("bot6", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6, plugins=dict(root="haku/modules"))
        bots.append(bot6)
    else:
        bots.append(None)

    if SESSION7:
        bot7 = Client("bot7", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7, plugins=dict(root="haku/modules"))
        bots.append(bot7)
    else:
        bots.append(None)

    if SESSION8:
        bot8 = Client("bot8", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8, plugins=dict(root="haku/modules"))
        bots.append(bot8)
    else:
        bots.append(None)

    if SESSION9:
        bot9 = Client("bot9", api_id=API_ID, api_hash=API_HASH, session_string=SESSION9, plugins=dict(root="haku/modules"))
        bots.append(bot9)
    else:
        bots.append(None)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create a logger for the bot
    logger = logging.getLogger("Hakutaka")

    # Configure a rotating file handler for the logger
    file_handler = RotatingFileHandler("bot.log", maxBytes=5 * 1024 * 1024, backupCount=2)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    for bot in bots:
        if bot is not None:
            await bot.start()

    await idle()
    await aiosession.close()
    logger.info("Haku is running!")


if __name__ == "__main__":
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(main())
