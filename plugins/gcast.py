# Copyright (C) 2021 By KAAL_KI_QUEEN

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "post", "send"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`sᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ ᴡᴀɪᴛ ʙᴀʙʏ ...`")
        if not message.reply_to_message:
            await wtf.edit("**__ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴀssᴀɢᴇ ᴛᴏ sᴛᴀʀᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ` \n\n**sᴇɴᴛ ᴛᴏ:** `{sent}` ᴄʜᴀᴛs \n**ғᴀɪʟᴇᴅ ɪɴ:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`ɢ ᴄᴀsᴛ sᴜᴄᴄᴇsғᴜʟʟʏ` \n\n**sᴇɴᴛ ᴛᴏ:** `{sent}` ᴄʜᴀᴛs \n**ғᴀɪʟᴇᴅ ɪɴ:** {failed} ᴄʜᴀᴛs")
