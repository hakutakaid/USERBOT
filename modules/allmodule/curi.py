import os
from pyrogram import Client, filters
from pyrogram.types import *
from modules.config import cmd

@Client.on_message(filters.command(["curi"], cmd) & filters.me)
async def pencuri(client, message):
    dia = message.reply_to_message
    me = client.me.id
    
    if not dia:
        await message.edit("`Mohon balas ke media.`")
        return  # Exit the function to prevent further execution

    anjing = dia.caption
    mmk = await message.edit("`Processing...`")
    await mmk.delete()

    if dia.text:
        await dia.copy(me)
        await message.delete()
    elif dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(me, anu, caption=anjing)
        await message.delete()
        os.remove(anu)
    elif dia.video:
        anu = await client.download_media(dia)
        await client.send_video(me, anu, caption=anjing)
        await message.delete()
        os.remove(anu)
    elif dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(me, anu, caption=anjing)
        await message.delete()
        os.remove(anu)
    elif dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(me, anu, caption=anjing)
        await message.delete()
        os.remove(anu)
    elif dia.document:
        anu = await client.download_media(dia)
        await client.send_document(me, anu, caption=anjing)
        await message.delete()
        os.remove(anu)

    try:
        await client.send_message(me, "`ini hasilnya tuan`")
    except Exception as e:
        print(e)
