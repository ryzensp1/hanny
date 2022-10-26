import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '7460290'))
API_HASH = environ.get('API_HASH', '40f25e810b628be54bcb44a58eb8d69e')
BOT_TOKEN = environ.get('BOT_TOKEN', '2034149452:AAE_TDxppP1SIvTY2NxQO0UvJ9AYbpimR_4')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1272039806').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001739340677 -1001519487578').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '2033197608').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001739340677')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
USE_AS_BOT = environ.get("USE_AS_BOT", True)

# maximum message length in Telegram
MAX_MESSAGE_LENGTH = 4096

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# the maximum number of 'selectable' messages in Telegram
TG_MAX_SELECT_LEN = environ.get("TG_MAX_SELECT_LEN", "100")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://moviesclub:chintamani2@cluster0.pwgvz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'McClustor')

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '👋 𝙷𝙴𝙻𝙾 {user}\n\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {bot},\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽...')
BTN_LOCK_ALERT = environ.get("BTN_LOCK_ALERT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒐 𝑼𝒔𝒆 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕!')
RemoveBG_API = environ.get("RemoveBG_API", "")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'mkn_bots_updates')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)



