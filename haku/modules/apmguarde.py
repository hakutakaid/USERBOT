"""
ᴍʏ ɢɪᴛʜuʙ : https://github.com/hakutakaid
ᴛʜᴀɴᴋs ᴛᴏ ᴢᴀɪᴅ-ᴜsᴇʀʙᴏᴛ

"""
from pyrogram import filters, Client
import asyncio
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users

import haku.database.pmpermitdb as Haku
from config import CMD as cmd

@Client.on_message(filters.command("pmguard", cmd) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**I only understand on or off**")
        return
    if arg == "off":
        await Haku.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await Haku.set_pm(True)
        await message.edit("**PM Guard Activated**")
@Client.on_message(filters.command("setpmmsg", cmd) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await Haku.set_permit_message(Haku.PMPERMIT_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await Haku.set_permit_message(f"`{arg}`")
    await message.edit("**Custom anti-pm message set**")