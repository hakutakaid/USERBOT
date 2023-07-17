from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
import asyncio
from haku.code.nganu import BL_GCAST

@Client.on_message(filters.me & filters.command("gcast", "."))
async def _(client, message: Message):
    sent = 0
    failed = 0
    user_id = client.me.id
    hasil = await message.reply(f"Sedang Memulai Gcast...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            if message.reply_to_message:
                send = message.reply_to_message
            elif len(message.command) < 2:
                return await hasil.edit(f"Berikan pesan atau balas ke pesan yang ingin anda broadcast")
            else:
                send = message.text.split(None, 1)[1]
            chat_id = dialog.chat.id
            if chat_id not in BL_GCAST:
                try:
                    if message.reply_to_message:
                        await send.copy(chat_id)
                    else:
                        await client.send_message(chat_id, send)
                    sent += 1
                    await asyncio.sleep(1)
                except Exception:
                    failed += 1
                    await asyncio.sleep(1)
    await hasil.edit(f"**𝐓𝐞𝐫𝐤𝐢𝐫𝐢𝐦 𝐊𝐞 : `{sent}` 𝐆𝐫𝐮𝐩 \n 𝐆𝐚𝐠𝐚𝐥 𝐊𝐢𝐫𝐢𝐦 𝐊𝐞: `{failed}` 𝐆𝐫𝐮𝐩**")
