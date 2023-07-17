import asyncio

from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from haku.code.nganu import *
from haku.code.base import *
from config import CMD as cmd

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(filters.me & filters.command(["setgpic"], cmd))
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await basic(message, f"`｢ᴋᴀᴍᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ {message.chat.title} ｣")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await basic(message, "`｢ʙᴀʟᴀs ᴋᴇ ᴘʜᴏᴛᴏ ᴜɴᴛᴜᴋ sᴇᴛ｣`")


@Client.on_message(filters.command(["ban", "dban"], cmd) & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    ky = await basic(message, "``")
    if not user_id:
        return await ky.edit("｢ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ｣")
    if user_id == client.me.id:
        return await ky.edit("｢ᴛɪᴅᴀᴋ ʙɪsᴀ ʙᴀɴɴᴇᴅ diri sendiri｣")
    if user_id in CREATOR:
        return await ky.edit("｢ᴏʀᴀɴɢ ɪɴɪ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪ ʙᴀɴ !!!!｣")
    if user_id in (await list_admins(client, message.chat.id)):
        return await ky.edit("｢ᴛɪᴅᴀᴋ ʙɪsᴀ ʙᴀɴɴᴇᴅ ᴀᴅᴍɪɴ｣")
    try:
        # await ky.delete()
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    msg = f"<b>｢ʙᴀɴɴᴇᴅ ᴜsᴇʀ｣:</b> {mention}\n<b>｢ʙᴀɴɴᴇᴅ ʙʏ｣:</b> {message.from_user.mention}\n"
    if reason:
        msg += f"<b>｢ʀᴇᴀsᴏɴ｣:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await ky.edit(msg)
    except ChatAdminRequired:
        return await ky.edit("**｢ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !｣**")


@Client.on_message(filters.command(["unban"], cmd) & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    zz = await basic(message, "`｢ᴘʀᴏᴄᴇssɪɴɢ...`")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await zz.edit("`ᴛɪᴅᴀᴋ ʙɪsᴀ unban ch`")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await zz.edit("｢ʙᴇʀɪᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ, ᴀᴛᴀᴜ ʀᴇᴘʟʏ ᴘᴇsᴀɴɴʏᴀ.｣")
    try:
        await message.chat.unban_member(user)
        await asyncio.sleep(0.1)
        # await zz.delete()
        umention = (await client.get_users(user)).mention
        await zz.edit(f"｢ᴜɴʙᴀɴɴᴇᴅ! {umention} ｣")
    except ChatAdminRequired:
        return await zz.edit("**｢ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !｣**")


@Client.on_message(filters.command(["pin", "unpin"], cmd) & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await basic(message, "｢ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴜɴᴛᴜᴋ ᴘɪɴ/ᴜɴᴘɪɴ.｣")
    await basic(message, "`｢ᴘʀᴏᴄᴇssɪɴɢ...`")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await basic(
            message,
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await basic(
            message,
            f"**Pinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        return await basic(message, "**｢ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !｣**")


@Client.on_message(filters.command(["mute"], cmd) & filters.me)
async def mute(client, message):
    user_id, reason = await extract_user_and_reason(message)
    nay = await basic(message, "`｢ᴘʀᴏᴄᴇssɪɴɢ...`")
    if not user_id:
        return await nay.edit("｢ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ｣")
    if user_id == client.me.id:
        return await nay.edit("｢ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴜᴛᴇ ᴅɪʀɪ sᴇɴᴅɪʀɪ｣")
    if user_id in CREATOR:
        return await nay.edit("ᴏʀᴀɴɢ ɪɴɪ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪ ᴍᴜᴛᴇ!!!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await nay.edit("ᴛɪᴅᴀᴋ ʙɪsᴀ mute admin.")
    # await nay.delete()
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**ᴍᴜᴛᴇᴅ ᴜsᴇʀ:** {mention}\n"
        f"**ᴍᴜᴛᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**｢ʀᴇᴀsᴏɴ｣:** {reason}"
    try:
        await message.chat.restrict_member(user_id, permissions=ChatPermissions())
        await nay.edit(msg)
    except ChatAdminRequired:
        return await nay.edit("**｢ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !｣**")


@Client.on_message(filters.command(["unmute"], cmd) & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    kl = await basic(message, "`｢ᴘʀᴏᴄᴇssɪɴɢ...`")
    if not user_id:
        return await kl.edit("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")
    try:
        await message.chat.restrict_member(user_id, permissions=unmute_permissions)
        # await kl.delete()
        umention = (await client.get_users(user_id)).mention
        await kl.edit(f"Unmuted! {umention}")
    except ChatAdminRequired:
        return await kl.edit("**｢ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !｣**")


@Client.on_message(filters.command(["kick", "dkick"], cmd) & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    ny = await basic(message, "`｢ᴘʀᴏᴄᴇssɪɴɢ...`")
    if not user_id:
        return await ny.edit("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")
    if user_id == client.me.id:
        return await ny.edit("ᴛɪᴅᴀᴋ ʙɪsᴀ ᴋɪᴄᴋ diri sendiri.")
    if user_id == CREATOR:
        return await ny.edit("ᴏʀᴀɴɢ ɪɴɪ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴅɪ ᴋɪᴄk")
    if user_id in (await list_admins(client, message.chat.id)):
        return await ny.edit("ᴛɪᴅᴀᴋ ʙɪsᴀ ᴋɪᴄᴋ admin.")
    # await ny.delete()
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**｢ᴋɪᴄᴋᴇᴅ ᴜsᴇʀ｣:** {mention}
**｢ᴋɪᴄᴋᴇᴅ ʙʏ｣:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**｢ʀᴇᴀsᴏɴ｣:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await ny.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await ny.edit("**｢ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !｣**")


@Client.on_message(
    filters.group & filters.command(["promote", "fullpromote"], cmd) & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    msg = await basic(message, "`｢ᴘʀᴏᴄᴇssɪɴɢ...`")
    if not user_id:
        return await msg.edit("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")
    (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    try:
        if message.command[0][0] == "f":
            await message.chat.promote_member(
                user_id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                ),
            )
            await asyncio.sleep(1)
            # await msg.delete()
            umention = (await client.get_users(user_id)).mention
            return await msg.edit(f"Fully Promoted! {umention}")

        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        await asyncio.sleep(1)
        # await msg.delete()
        umention = (await client.get_users(user_id)).mention
        await msg.edit(f"Promoted! {umention}")
    except ChatAdminRequired:
        return await msg.edit("**｢ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ !｣**")


@Client.on_message(
    filters.group
    & filters.command(["cdemote"], [cmd])
    & filters.user(CREATOR)
    & ~filters.me
)
@Client.on_message(filters.group & filters.command(["demote"], cmd) & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    msg = await basic(message, "`｢ᴘʀᴏᴄᴇssɪɴɢ...`")
    if not user_id:
        return await msg.edit("ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ")
    if user_id == client.me.id:
        return await msg.edit("ᴛɪᴅᴀᴋ ʙɪsᴀ demote diri sendiri.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    await asyncio.sleep(1)
    # await msg.delete()
    umention = (await client.get_users(user_id)).mention
    await msg.edit(f"Demoted! {umention}")