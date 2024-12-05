import logging
from logging.handlers import RotatingFileHandler
import os

PORT = "8080"

BOT_TOKEN = os.environ.get("BOT_TOKEN" , "")

API_ID = os.environ.get("API_ID" , "")

API_HASH = os.environ.get( "API_HASH" , "")

CHANNEL_ID = -1001945210884

OWNER = [6389186248]

ADMINS = []

ADMINS.extend(OWNER)

DB_URI = os.environ.get( "DB_URI" , "")

DB_NAME = "binge"

FSUB_CHANNEL = -1001924763706

CUSTOM_CAPTION = '''<b>{previouscaption}

➤ Jᴏɪɴ Aɴᴅ Sᴜᴘᴘᴏʀᴛ~
@Binge_Pirates</b>'''

PROTECT_CONTENT = False

DISABLE_CHANNEL_BUTTON = True

SHORTENER_API = os.environ.get("SHORTENER_API" , "")

SHORTENER_SITE = "gyanilinks.com"

HOW_TO_DOWNLOAD = "https://telegram.me/How_To_Download_From_Linkz/4"

TIMEOUT = 3600

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "log.txt",
            mode = "w",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
