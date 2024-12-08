from bot import Bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from config import *
from db import *
from helper import *
import asyncio
from datetime import datetime
import random , string
import time

async def handle_token(app , message , b64):
    user_id = str(message.from_user.id)
    if 'TOKEN' not in cf: cf['TOKEN'] = {}
    if user_id not in cf['TOKEN']: cf['TOKEN'][user_id] = {}
    token = cf['TOKEN'][user_id].get('TOKEN')
    tim = cf['TOKEN'][user_id].get('TIME')
    if (not tim) or ((int(time.time()) - tim) > 0 ):
        if token: link = f'https://telegram.me/{app.me.username}?start=token{token}'
        else:
            token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
            link = f'https://telegram.me/{app.me.username}?start=token{token}'
            cf['TOKEN'][user_id]['TOKEN'] = token
        LOGGER(__name__).info(f'Token Generated For {message.from_user.first_name} - https://t.me/{app.me.username}?start=token{token}')
        short = await short_url(link)
        await message.reply_text(f'''<b>Hey {message.from_user.mention} , Your Ads Pass Is Expired , Please Go Through The Link Again !

After Passing Link You Don't Need To Pass Ad Again For Next {await get_readable_time(TIMEOUT)} !</b>''' , reply_markup = InlineKeyboardMarkup(
    [
        [   
            InlineKeyboardButton('Link', url = short) ,
            InlineKeyboardButton('Tutorial', url = HOW_TO_DOWNLOAD)
        ],
        [
            InlineKeyboardButton('Try Again ↻', url = f'https://telegram.me/{app.me.username}?start={b64}') ,
        ]
    ]
) , quote=True)
        await sync()
        return True
    return False

async def settle_token(app , message , token_):
    user_id = str(message.from_user.id)
    if 'TOKEN' not in cf: cf['TOKEN'] = {}
    if user_id not in cf['TOKEN']: cf['TOKEN'][user_id] = {}
    token = cf['TOKEN'][user_id].get('TOKEN')
    if (not token) or token != token_:
        return await message.reply_text('<b>Not Your Token Or Token Invalid !</b>',quote=True)
    cf['TOKEN'][user_id]['TIME'] = int(time.time()) + TIMEOUT
    await message.reply_text(f'''<b>Link ByPassed Successfully For Next {await get_readable_time(TIMEOUT)}!
    
Now Press The Try Again Button Above Or Click Link Again From The Channel</b>''' , quote=True)
    del cf['TOKEN'][user_id]['TOKEN']
    await sync()

@Bot.on_message(filters.command('start') & filters.private)
async def start(app , message):
    id_ = message.from_user.id
    if id_ not in cf.get('users' , []):
        if 'users' not in cf: cf['users'] = []
        cf['users'].append(id_)
    subscribed = await is_subscribed(app , message)
    if not subscribed:
        reply_markup = [
            [ InlineKeyboardButton( "Cʜᴀɴɴᴇʟ  ⚡️", url = app.invitelink) ] ,
        ]
        try:
            reply_markup[-1].append(
                InlineKeyboardButton( 'Tʀʏ Aɢᴀɪɴ 🔄', url = f"https://t.me/{app.me.username}?start={message.command[1]}")
            )
        except: pass
        await message.reply_text(f'''<b>👋 Hᴇʟʟᴏ {message.from_user.mention} !

🔗 Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ Tᴏ Usᴇ Mᴇ

🙏 Kɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟ</b>''' , reply_markup = InlineKeyboardMarkup(reply_markup) , quote = True)
        return await sync()
    text = message.text.split(maxsplit=1)
    if len(text) > 1 and text[1].startswith('token'):
        await settle_token(app , message , text[1].replace('token',''))
        return
    if len(text) == 1:
        reply_markup = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("😊 Aʙᴏᴜᴛ Mᴇ", callback_data = "about"),
                    InlineKeyboardButton("🔒 cʟᴏsᴇ", callback_data = "close")
                ]
            ])
        await message.reply_text(f'''<b>👋 Gʀᴇᴇᴛɪɴɢs , {message.from_user.mention} !  

🤖 I'ᴍ Mᴏʀᴇ Tʜᴀɴ Jᴜsᴛ A Bᴏᴛ! I'ᴍ A Cᴜsᴛᴏᴍ Cʀᴇᴀᴛɪᴏɴ Bʏ @Binge_Pirates , Aɴᴅ Mʏ Mɪssɪᴏɴ Is Tᴏ Dᴇʟɪᴠᴇʀ Mᴏᴠɪᴇs 🎬 Aɴᴅ Sᴇʀɪᴇs 📺 Rɪɢʜᴛ Tᴏ Yᴏᴜʀ Fɪɴɢᴇʀᴛɪᴘs, Sᴘᴇᴄɪᴀʟʟʏ Dᴇsɪɢɴᴇᴅ Fᴏʀ Yᴏᴜʀ Eɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ! 🍿📤

🌟 Pᴏᴡᴇʀᴇᴅ Bʏ ~ @Binge_Pirates</b>''' , reply_markup = reply_markup , quote=True)
        await sync()
    elif len(text) == 2:
        if text[1] == 'premium':
            text = '''<b>🌟 Wᴇʟᴄᴏᴍᴇ Tᴏ Oᴜʀ Exᴄʟᴜsɪᴠᴇ Bɪɴɢᴇ Pʀᴇᴍɪᴜᴍ Cʜᴀɴɴᴇʟ ! 🍿✨  
🎁 Cʜᴏᴏsᴇ Yᴏᴜʀ Pʟᴀɴ: 
----💸 𝟷𝟶 Rs Wᴇᴇᴋʟʏ  
----💰 𝟹𝟶 Rs Mᴏɴᴛʜʟʏ   
----⏳ 𝟿𝟶 Rs Fᴏʀ 𝟹 Mᴏɴᴛʜs  
----📆 𝟷𝟸𝟶 Rs Fᴏʀ 𝟼 Mᴏɴᴛʜs  
----🌟 𝟸𝟺𝟶 Rs Fᴏʀ A Yᴇᴀʀ

Pᴀʏᴍᴇɴᴛs Cᴀɴ Bᴇ Mᴀᴅᴇ Sᴇᴄᴜʀᴇʟʏ Tʜʀᴏᴜɢʜ Oᴜʀ Bᴏᴛ. 
🚀 Hᴏᴡ Tᴏ Sᴜʙsᴄʀɪʙᴇ : Cʜᴇᴄᴋ Tʜᴇ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ

🌟 Pᴏᴡᴇʀᴇᴅ Bʏ ~ @Binge_Pirates</b>'''
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("Pᴀʏᴍᴇɴᴛ Pʀᴏᴄᴇss",url="https://t.me/Binge_Premium/2")],
                [InlineKeyboardButton("Cᴏɴᴛᴀᴄᴛ Fᴏʀ Qᴜᴇʀɪᴇs Oɴ Pʀᴇᴍɪᴜᴍ",url="https://telegram.me/Binge_Admin/3")]
            ])
            await message.reply_photo("https://mytoastlife.com/wp-content/uploads/2021/06/summer-classic-film-series.jpg", caption=text , reply_markup=reply_markup , quote=True)
            await sync()
        else:
            base64_string = text[1]
            if base64_string.startswith('short'):
                tk = base64_string.replace('short' , '')
                base64_string = cf.get('shorten',{}).get(tk)
            if not base64_string: return await sync()
            string = await decode(base64_string)
            argument = string.split("-")
            ids = await get_msg_ids(app , argument)
            if not ids: return await sync()
            temp_msg = await message.reply("<b>Pʟᴇᴀsᴇ Wᴀɪᴛ...</b>",quote=True)
            try:
                messages = await get_messages(app, ids)
            except:
                await temp_msg.edit_text("<b>Sᴏᴍᴇᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ Pʟᴇᴀsᴇ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ..!</b>")
                return await sync()
            await temp_msg.delete()
            if "#Sample_Video" not in (messages[0].text or messages[0].caption) and message.from_user.id not in ADMINS:
                status = await handle_token(app , message , base64_string)
                if status: return
            if not messages: return await sync()
            for msg in messages:
                if bool(CUSTOM_CAPTION) & bool(msg.document or msg.video):
                    caption = CUSTOM_CAPTION.format( previouscaption = "" if not msg.caption else msg.caption.html )
                else:
                    caption = "" if not msg.caption else msg.caption.html
                reply_markup = msg.reply_markup
                try:
                    await msg.copy(chat_id=message.from_user.id, caption = caption, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                    await asyncio.sleep(0.5)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    await msg.copy(chat_id=message.from_user.id, caption = caption, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                except:
                    pass
#############################################################################################
            if not "#Sample_Video" in (messages[0].text or messages[0].caption):
                await asyncio.sleep(0.5)
                await message.reply_text(f'''<b>Tʜᴀɴᴋ Yᴏᴜ 🙏 Fᴏʀ Usɪɴɢ Oᴜʀ Cʜᴀɴɴᴇʟ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Tʜᴇsᴇ Fɪʟᴇs.

Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Iɴ A Cʜᴀɴɴᴇʟ Cʜᴇᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ.

🌟 Powered By :- <a href='https://t.me/Binge_Pirates'>Binge Pirates</a></b>''', disable_web_page_preview=True ,reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('Cʜᴀɴɴᴇʟ  ⚡️',url='https://telegram.me/Binge_Pirates')],
                [InlineKeyboardButton('Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs 📁',callback_data="premium")]
            ]))
#############################################################################################
            await sync()
            app.LOGGER(__name__).info(f"{message.from_user.first_name} [{message.from_user.id}] Got {len(messages)} Files With B64 {base64_string} !")

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client , message):
    await message.reply_text(f"<b>{len(cf.get('users',[]))} users are using this bot !</b>" , True)

@Bot.on_message(filters.command('log') & filters.private & filters.user(ADMINS))
async def log(client , message):
    await message.reply_document("log.txt" , caption = "<b>Log File</b>" , quote=True)

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot, message):
    now = datetime.now()
    delta = now - bot.uptime
    time = await get_readable_time(delta.seconds)
    await message.reply(f'<b>BOT UPTIME\n{time}</b>' , True)

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client, message):
    if message.reply_to_message:
        query = cf['users']
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        stats_text = """<b><u>Broadcast Processing</u>

Total Users: <code>{}</code>
Successful: <code>{}</code>
Blocked Users: <code>{}</code>
Deleted Accounts: <code>{}</code>
Unsuccessful: <code>{}</code></b>"""
        pls_wait = await message.reply_text("<b><i>Broadcasting Message.. This will Take Some Time</i></b>" , True)
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
                await asyncio.sleep(2)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                cf['users'].remove(chat_id)
                blocked += 1
            except InputUserDeactivated:
                cf['users'].remove(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
            await sync()
            if total % 3 == 0: await pls_wait.edit( stats_text.format(total , successful , blocked , deleted , unsuccessful) )
        await pls_wait.delete()
        return await message.reply_text( stats_text.replace('Processing' , 'Completed').format(total , successful , blocked , deleted , unsuccessful) , True )
    else:
        await message.reply_text("""<code>Use this command as a replay to any telegram message with out any spaces.</code>""" , True)
