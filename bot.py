from pyrogram import Client
import sys
from datetime import datetime
from aiohttp import web
from plugins import web_server

from config import *

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="bingefilestore",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={
                "root": "plugins"
            },
            workers=4,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER
    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.uptime = datetime.now()
        if FSUB_CHANNEL:
            try:
                link = (await self.get_chat(FSUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FSUB_CHANNEL)
                    link = (await self.get_chat(FSUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FSUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped.")
                sys.exit()
        try:
            self.db_channel = await self.get_chat(CHANNEL_ID)
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped.")
            sys.exit()
        self.LOGGER(__name__).info(f"Bot Running..!")

        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        
    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")