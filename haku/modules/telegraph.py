"""
My Telegeram : https://t.me/Hakutaka_id
My Github : 
Thanks To
@Kenapanan

"""


from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file
from haku.code.nganu import *
from config import CMD as cmd
import os


telegraph = Telegraph()
r = telegraph.create_account(short_name="telegram")
auth_url = r["auth_url"]



def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
        
@Client.on_message(filters.user(CREATOR) & filters.command("ctg", ".") & ~filters.me)
@Client.on_message(filters.command(["tg", "telegraph", "tm", "tgt"], cmd) & filters.me)
async def uptotelegraph(client: Client, message: Message):
    tex = await message.edit_text("`Processing . . .`")
    if not message.reply_to_message:
        await tex.edit(
            "**｢ᴍᴏʜᴏɴ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴀᴛᴀᴜ ᴍᴇᴅɪᴀ !｣**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**｢ᴍᴀᴀғ ᴇʀʀᴏʀ !｣:** `{exc}`")
            os.remove(m_d)
            return
        Sukses = (
            f"**Uploaded on ** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await tex.edit(Sukses)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**｢ᴍᴀᴀғ ᴇʀʀᴏʀ !｣:** `{exc}`")
            return
        upludi = f"**Uploaded as** [Telegraph](https://telegra.ph/{response['path']})"
        await tex.edit(upludi)