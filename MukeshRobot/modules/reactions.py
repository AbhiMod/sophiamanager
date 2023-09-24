import random

from telegram import Update
from telegram.ext import CallbackContext

from MukeshRobot import dispatcher
from MukeshRobot.modules.disable import DisableAbleCommandHandler

reactions = [
   "⚡️ ᴘʀɪᴄᴇ ᴏꜰ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴍʙᴇʀꜱ 100% ɴᴏɴ ᴅʀᴏᴘ
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
⌛️ ꜱᴛᴀʀᴛ ᴛɪᴍᴇ : 1 - 8 ʜᴏᴜʀ

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

ʏᴏᴜ ᴡᴀɴᴛ ᴀᴅᴅ ᴍᴇᴍʙᴇʀꜱ ᴅᴍ  : @AM_YTBOTT",
]


def react(update: Update, context: CallbackContext):
    message = update.effective_message
    react = random.choice(reactions)
    if message.reply_to_message:
        message.reply_to_message.reply_text(react)
    else:
        message.reply_text(react)


REACT_HANDLER = DisableAbleCommandHandler("price", react, run_async=True)

dispatcher.add_handler(REACT_HANDLER)

__command_list__ = ["price"]
__handlers__ = [REACT_HANDLER]
