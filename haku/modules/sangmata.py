"""
My Telegeram : https://t.me/Hakutaka_id
My Github : 
Thanks To
@Kenapanan
"""

import asyncio

from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.raw.functions.messages import DeleteHistory
from haku.code.base import *
from config import CMD as cmd

@Client.on_message(filters.me & filters.command("sg", cmd))
async def _(client, message):
    args = await extract_user(message)
    lol = await basic(message, "Sedang Memproses...")
    if args:
        try:
            user = await client.get_users(args)
        except Exception as error:
            return await lol.edit(error)
    bot = "SangMata_BOT"
    try:
        txt = await client.send_message(bot, f"{user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        txt = await client.send_message(bot, f"{user.id}")
    await txt.delete()
    await asyncio.sleep(5)
    await lol.delete()
    async for stalk in client.search_messages(bot, query="History", limit=1):
        if not stalk:
            NotFound = await client.send_message(client.me.id, "Tidak ada komentar")
            await NotFound.delete()
        else:
            await message.reply(stalk.text)
    user_info = await client.resolve_peer(bot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
