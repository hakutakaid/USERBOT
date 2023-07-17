from pyrogram import Client, filters
from datetime import datetime
from haku.code.nganu import CREATOR
from config import CMD as cmd

@Client.on_message(filters.user(CREATOR) & filters.command("cping", "") & ~filters.me)
@Client.on_message(filters.me & filters.command("ping", cmd))
async def ping_pong(client, message):
    start_time = datetime.now()
    pong_message = await message.reply("...Pong!")
    end_time = datetime.now()
    ms = (end_time - start_time).microseconds / 1000
    await pong_message.edit_text(f"❑ ｢ᴘᴏɴɢ! \n{ms} ᴍs｣")
