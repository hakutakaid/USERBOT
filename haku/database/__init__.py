"""
ᴍʏ ɢɪᴛʜᴜʙ : https://github.com/hakutakaid
ᴛʜᴀɴᴋs ᴛᴏ ᴢᴀɪᴅ-ᴜsᴇʀʙᴏᴛ

"""

import motor.motor_asyncio
from pyrogram import *
from config import MONGO_URL
cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

dbb = cli.program
notesdb = cli.notes
logdb = cli.gruplog
