"""
My Telegeram : https://t.me/Hakutaka_id
My Github : @Hakutaka1234
Thanks To
@Kenapanan
"""

import os

from pyrogram import *
from pyrogram import filters
from pyrogram.types import *
from config import CMD as cmd
@Client.on_message(filters.command(["curi"], cmd) & filters.me)
async def pencuri(client, message):
    fromuserreply = message.reply_to_message
    user_id = client.me.id
    me = client.me.id
    if not fromuserreply:
        await client.send_message(me, "`Mohon balas ke mefromuserreply.`")
    njir = fromuserreply.caption or None
    zzx = await message.edit("`Processing...`")
    await zzx.delete()
    if fromuserreply.text:
        await fromuserreply.copy(me)
        await message.delete()
    if fromuserreply.photo:
        zz = await client.download_mefromuserreply(fromuserreply)
        await client.send_photo(me, zz, njir)
        await message.delete()
        os.remove(zz)
    if fromuserreply.video:
        zz = await client.download_mefromuserreply(fromuserreply)
        await client.send_video(me, zz, njir)
        await message.delete()
        os.remove(zz)
    if fromuserreply.audio:
        zz = await client.download_mefromuserreply(fromuserreply)
        await client.send_audio(me, zz, njir)
        await message.delete()
        os.remove(zz)
    if fromuserreply.voice:
        zz = await client.download_mefromuserreply(fromuserreply)
        await client.send_voice(me, zz, njir)
        await message.delete()
        os.remove(zz)
    if fromuserreply.document:
        zz = await client.download_mefromuserreply(fromuserreply)
        await client.send_document(me, zz, njir)
        await message.delete()
        os.remove(zz)
    try:
        await client.send_message(me, "**Pap timernya tuh.**")
    except Exception as e:
        print(e)

