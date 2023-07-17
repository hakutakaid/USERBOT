import os

from gpytranslate import Translator
from pyrogram import filters
from pyrogram import Client
from config import CMD as cmd
@Client.on_message(filters.me & filters.command(["tr", "tl"], cmd))
async def _(client, message):
    trans = Translator()
    if message.reply_to_message:
        dest = "id" if len(message.command) < 2 else message.text.split(None, 2)[1]
        to_translate = message.reply_to_message.text or message.reply_to_message.caption
    else:
        if len(message.command) < 3:
            return
        dest = message.text.split(None, 2)[1]
        to_translate = message.text.split(None, 2)[2]
    source = await trans.detect(to_translate)
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = f"<b>Bahasa {source} Ke Bahasa {dest}</b>:\n<code>{translation.text}</code>"
    reply_me_or_user = message.reply_to_message or message
    await client.send_message(
        message.chat.id, reply, reply_to_message_id=reply_me_or_user.id
    )
