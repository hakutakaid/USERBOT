"""
https://t.me/Hakutaka_id

"""

from pyrogram import *
from pyrogram import filters
from pyrogram.enums import ChatType

from haku.code.base import *
from config import CMD as cmd


@Client.on_message(filters.me & filters.command("id", cmd))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == ChatType.PRIVATE:
        user_id = message.chat.id
        await basic(
            message,
            f"◈ <b> ｢ɪᴅ｣</b> <code>{user_id}</code>",
        )
    if chat_type == ChatType.CHANNEL:
        await basic(
            message,
            f"◈ <b> ｢ɪᴅ｣ {message.sender_chat.title}:</b> <code>{message.sender_chat.id}</code>",
        )
    elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        _id = ""
        _id += f"◈ <b> ｢ɪᴅ｣ {message.chat.title}:</b> <code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                f"◈ <b> ｢ɪᴅ｣ {message.reply_to_message.from_user.first_name} Adalah:</b> "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            if file_info := get_file_id(message.reply_to_message):
                _id += (
                    f"◈ <b> ｢ɪᴅ｣ {file_info.message_type}:</b> "
                    f"<code>{file_info.file_id}</code>\n"
                )
        else:
            _id += f"◈ <b> ｢ɪᴅ｣ {message.from_user.first_name}:</b> <code>{message.from_user.id}</code>\n"
            if file_info := get_file_id(message):
                _id += (
                    f"<b>{file_info.message_type}</b>: "
                    f"<code>{file_info.file_id}</code>\n"
                )
        m = message.reply_to_message or message
        await basic(m, _id)