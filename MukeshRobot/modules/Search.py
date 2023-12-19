import glob
import io
import os
import random

import requests
from PIL import Image, ImageDraw, ImageFont
from MukeshRobot.modules.nightmode import button_row
from MukeshRobot import BOT_USERNAME, OWNER_ID,BOT_NAME, SUPPORT_CHAT, telethn
from MukeshRobot.events import register


__mod_name__ = "ɢᴏᴏɢʟᴇ-sᴇᴀʀᴄʜ"

__help__ = """
sᴇᴀʀᴄʜɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ

❍ /google : sᴇᴀʀᴄʜɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ...
❍ /stack : sᴇᴀʀᴄʜɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ...
"""
