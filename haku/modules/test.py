"""
My Telegeram : https://t.me/Hakutaka_id
My Github : 
"""

from pyrogram import Client, filters
from haku.code.nganu import CREATOR

@Client.on_message(filters.user(CREATOR) & filters.command("nganu", ""))
async def haku(client, message):
    await message.react(emoji="👻")
