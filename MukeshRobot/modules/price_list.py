import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG
from pyrogram import Client, filters

# Define a command handler
@pbot.on_message(filters.command("price"))
async def start_command(client, message):
    await message.reply("""
⚡️ ᴘʀɪᴄᴇ ᴏꜰ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴍʙᴇʀꜱ 100% ɴᴏɴ ᴅʀᴏᴘ ⚡️
1. 60ʀꜱ 1ᴋ ᴍᴇᴍʙᴇʀꜱ ʟᴏᴡ ᴘʀɪᴄᴇ
💨ꜱᴛᴀʀᴛ - ɪɴꜱᴛᴀɴᴛ ᴛᴏ 30ᴍɪɴᴜᴛᴇꜱ
🚀ꜱᴘᴇᴇᴅ - 100ᴋʀᴇᴀʟ ᴅᴀɪʟʏ ꜱᴘᴇᴇᴅ
❤️ɢᴜᴀʀᴀɴᴛᴇᴇ - [ɴᴏ ɢᴜᴀʀᴀɴᴛᴇᴇ]
❤️‍🔥Qᴜᴀʟɪᴛʏ - ᴍᴏꜱᴛ ᴇɴɢʟɪꜱʜ ɴᴀᴍᴇ ᴀᴄᴄᴏᴜɴᴛ
☑️ᴄʜᴀɴɴᴇʟ + ɢʀᴏᴜᴘ

2. 100ʀꜱ 1ᴋ ᴍᴇᴍʙᴇʀꜱ
✅ 100% ʀᴇᴀʟ ᴍᴇᴍʙᴇʀꜱ
✅ ꜱᴜɪᴛᴀʙʟᴇ ꜰᴏʀ ᴀʟʟ ɢᴇᴏ ᴏᴡɴᴇʀ
✅ ꜰʀᴇꜱʜ ʟɪɴᴋ ꜱᴜᴘᴘᴏʀᴛ [ɴᴇᴡ ᴄʜᴀɴɴᴇʟ & ɢʀᴏᴜᴘ]
⛔️ ɴᴏ ʀᴇꜰɪʟʟ / ɴᴏ ɢᴜᴀʀᴀɴᴛᴇᴇ
⌛ ꜱᴛᴀʀᴛ ᴛɪᴍᴇ : 1 - 8 ʜᴏᴜʀ

4. 120ʀꜱ 1ᴋ ᴍᴇᴍʙᴇʀꜱ ᴍɪᴅᴅʟᴇ ᴘʀɪᴄᴇ
⚡️ ꜱᴛᴀʀᴛ - ɪɴꜱᴛᴀɴᴛ ᴛᴏ 30ᴍɪɴᴜᴛᴇꜱ
⚡️ ꜱᴘᴇᴇᴅ - 150ᴋ ʀᴇᴀʟ ᴅᴀɪʟʏ ꜱᴘᴇᴇᴅ
⚡️ ɢᴜᴀʀᴀɴᴛᴇᴇ - ʟɪꜰᴇᴛɪᴍᴇ 0% ᴅʀᴏᴘ [3 ᴍᴏɴᴛʜ ɢᴜᴀʀᴀɴᴛᴇᴇ]
⚡️ Qᴜᴀʟɪᴛʏ - ᴍᴏꜱᴛ ᴇɴɢʟɪꜱʜ ɴᴀᴍᴇ ᴀᴄᴄᴏᴜɴᴛ
⚡️ ᴄʜᴀɴɴᴇʟ + ɢʀᴏᴜᴘ

5. 180ʀꜱ 1ᴋ ᴍᴇᴍʙᴇʀꜱ
🔥 ꜱᴛᴀʀᴛ - ɪɴꜱᴛᴀɴᴛ ᴛᴏ 30ᴍɪɴᴜᴛᴇꜱ
🔥 ꜱᴘᴇᴇᴅ - 50ᴋ ʀᴇᴀʟ ᴅᴀɪʟʏ ꜱᴘᴇᴇᴅ
🔥 ɢᴜᴀʀᴀɴᴛᴇᴇ - [12 ᴍᴏɴᴛʜ ɢᴜᴀʀᴀɴᴛᴇᴇ]
🔥 ᴀʟʟ ꜱᴜʙᴊᴇᴄᴛ + ᴀʟʟ ᴏᴡɴᴇʀ ᴀʀᴇ ᴀᴄᴄᴇᴘᴛᴇᴅ
🔥 ʙᴀꜱᴇ - 500ᴋ
🔥 ᴄʜᴀɴɴᴇʟ + ɢʀᴏᴜᴘ
🔥 ʙᴇꜱᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴍʙᴇʀꜱ

ɴᴏᴛᴇ : ɪꜰ ʏᴏᴜ ᴏᴅᴇʀ ʙᴜʟʟᴋ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴅɪꜱᴄᴏᴜɴᴛ. 

ʏᴏᴜ ᴡᴀɴᴛ ᴀᴅᴅ ᴍᴇᴍʙᴇʀꜱ ᴅᴍ ᴛᴏ [ᴀᴍʙᴏᴛ](https://t.me/AM_YTBOTT) : @AM_YTBOTT
ꜱᴜᴘᴘᴏʀᴛ [ᴄʜᴀɴɴᴇʟ1](https://t.me/AbhiModszYT_Return)
ꜱᴜᴘᴘᴏʀᴛ [ᴄʜᴀɴɴᴇʟ2](https://t.me/AmBotYT)
ꜱᴜᴘᴘᴏʀᴛ [ɢʀᴏᴜᴘ](https://t.me/AM_YTSUPPORT)
""")
    

