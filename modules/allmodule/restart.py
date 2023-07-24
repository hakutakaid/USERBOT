import subprocess
import os
from pyrogram import Client, filters
from pyrogram import *
from modules.config import cmd
import asyncio

@Client.on_message(filters.me & filters.command("restart", cmd))
async def restart_system(client, message):
    x = await message.reply(f"`restarting....`", quote=True)
    await asyncio.sleep(1)
    await x.edit(f"`Tunggu Ya... Sistem Sedang Di Restart...`")
    await asyncio.sleep(1)
    await message.delete()
    await x.delete()
    subprocess.run(["python3", "-B", "-m", "bot"])