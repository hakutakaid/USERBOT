from haku.database import notesdb
from pyrogram import filters
from pyrogram.filters import chat
from pyrogram.types import Message
from config import noteslog as nganu

user_id = nganu

async def get_botlog(user_id: int):
    user_data = await logdb.users.find_one({"user_id": user_id})
    botlog_chat_id = user_data.get("bot_log_group_id") if user_data else None
    return botlog_chat_id


async def get_notes_count() -> dict:
    chats_count = 0
    notes_count = 0
    async for chat in notesdb.find({"user_id": {"$exists": 1}}):
        notes_name = await get_note_names(chat["user_id"])
        notes_count += len(notes_name)
        chats_count += 1
    return {"chats_count": chats_count, "notes_count": notes_count}


async def _get_notes(user_id: int) -> Dict[str, int]:
    _notes = await notesdb.find_one({"user_id": user_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_note_names(user_id: int) -> List[str]:
    _notes = []
    for note in await _get_notes(user_id):
        _notes.append(note)
    return _notes


async def get_note(user_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_notes(user_id)
    if name in _notes:
        return _notes[name]
    return False


async def save_note(user_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_notes(user_id)
    _notes[name] = note

    await notesdb.update_one(
        {"user_id": user_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_note(user_id: int, name: str) -> bool:
    notesd = await _get_notes(user_id)
    name = name.lower().strip()
    if name in notesd:
        del notesd[name]
        await notesdb.update_one(
            {"user_id": user_id},
            {"$set": {"notes": notesd}},
            upsert=True,
        )
        return True
    return False