"""
ᴍʏ ɢɪᴛʜᴜʙ : https://github.com/hakutakaid
ᴛʜᴀɴᴋs ᴛᴏ ᴢᴀɪᴅ-ᴜsᴇʀʙᴏᴛ

"""

from haku.database import cli
import asyncio

collection = cli["Haku"]["pmpermit"]

PMPERMIT_MESSAGE = (
    f"📣 **PESAN PENTING** 📣\n\n"
    f"⚠️ ᴘᴇʀɪɴɢᴀᴛᴀɴ !!! ᴊᴀɴɢᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ sᴘᴀᴍ! ⚠️\n"
    f"🚫 sᴇʙᴇʟᴜᴍ ᴅɪ ᴀᴄᴄ sᴀᴍᴀ ᴛᴜᴀɴ sᴀʏᴀ\n"
    f"    ᴀᴛᴀᴜ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴅɪ ʙʟᴏᴄᴋ!! 🚫\n"
    f"🤖 ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs ʙʏ χнαχнυ υѕєявσт 🤖"
)


BLOCKED = "``ᴍᴀᴀғ ᴀɴᴅᴀ sᴀʏᴀ ʙʟᴏᴄᴋɪʀ !\n ᴋᴀʀᴇɴᴀ ᴍᴇʟᴀᴋᴜᴋᴀɴ sᴘᴀᴍ !``"

LIMIT = 5


async def set_pm(value: bool):
    doc = {"_id": 1, "pmpermit": value}
    doc2 = {"_id": "Approved", "users": []}
    r = await collection.find_one({"_id": 1})
    r2 = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": 1}, {"$set": {"pmpermit": value}})
    else:
        await collection.insert_one(doc)
    if not r2:
        await collection.insert_one(doc2)


async def set_permit_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"pmpermit_message": text}})


async def set_block_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"block_message": text}})


async def set_limit(limit):
    await collection.update_one({"_id": 1}, {"$set": {"limit": limit}})


async def get_pm_settings():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    pmpermit = result["pmpermit"]
    pm_message = result.get("pmpermit_message", PMPERMIT_MESSAGE)
    block_message = result.get("block_message", BLOCKED)
    limit = result.get("limit", LIMIT)
    return pmpermit, pm_message, limit, block_message


async def allow_user(chat):
    doc = {"_id": "Approved", "users": [chat]}
    r = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": "Approved"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_approved_users():
    results = await collection.find_one({"_id": "Approved"})
    if results:
        return results["users"]
    else:
        return []


async def deny_user(chat):
    await collection.update_one({"_id": "Approved"}, {"$pull": {"users": chat}})


async def pm_guard():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    if not result["pmpermit"]:
        return False
    else:
        return True
