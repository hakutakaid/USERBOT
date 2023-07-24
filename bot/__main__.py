#created By Hakutakaid
from bot import *
async def main():
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("modules" + all_module)
        print(f"🏠 Berhasil Mengimpor {all_module} 🎴")
    for cli in clients:
        await cli.start()
        ex = await cli.get_me()
        LOGGER("✓").info(f"🏠 Bot Berjalan Di {ex.first_name} | {ex.id} ")
        ids.append(ex.id)
        await cli.send_message("me", f"`🇮🇩 PyroBot Telah Di Aktifkan` ...\n\n**🎴 Pyrogram Version** : `{vp}`\n\n**🏠 Created By :** {ex.mention}")
    try:
        await cli.join_chat("asukamuyaas")
    except BaseException as e:
        LOGGER("Info").warning(f"{e}") 
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
