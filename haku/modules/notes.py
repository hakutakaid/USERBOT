from asyncio import sleep
from pyrogram import Client, filters
from haku.database.notes import *
from pyrogram.types import Message
from .pmguard import get_arg, denied_users


@Client.on_message(filters.me & filters.command("save", "."))
async def simpan_note(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("`Silakan balas ke pesan.`")
    anu = await msg.forward(client.me.id)
    msg_id = anu.id
    await client.send_message(client.me.id,
        f"#NOTE\nKEYWORD: {name}"
        "\n\nPesan berikut disimpan sebagai data balasan catatan untuk obrolan, mohon jangan dihapus !!",
    )
    await sleep(1)
    await save_note(user_id, name, msg_id)
    await message.reply(f"**Berhasil menyimpan catatan dengan nama** `{name}`")


@Client.on_message(filters.me & filters.command("get", "."))
async def panggil_notes(client, message):
    name = get_arg(message)
    user_id = message.from_user.id
    _note = await get_note(user_id, name)
    if not _note:
        return await message.reply("`Tidak ada catatan seperti itu.`")
    msg_o = await client.get_messages(client.me.id, _note)
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)

