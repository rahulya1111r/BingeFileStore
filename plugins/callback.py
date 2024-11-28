from pyrogram import __version__
from bot import Bot
from config import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Bot.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f'''<b>👤 Cʀᴇᴀᴛᴏʀ: <a href='tg://user?id={OWNER[0]}'>Tʜɪs Pᴇʀsᴏɴ</a>

📜 Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3 

📚 Lɪʙʀᴀʀɪᴇs: Pʏʀᴏɢʀᴀᴍ Asʏɴᴄɪᴏ V{__version__}

📢 Cʜᴀɴɴᴇʟ: @Binge_Pirates 

🤝 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ: <a href='https://t.me/+HziAXCYexzNiMzE5'>Cʟɪᴄᴋ Hᴇʀᴇ</a></b>''',
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                        [InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data = "back"),
                        InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close")]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "back":
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😊 Aʙᴏᴜᴛ Mᴇ", callback_data = "about"),
                    InlineKeyboardButton("🔒 cʟᴏsᴇ", callback_data = "close")
                ]
            ]
        )
        await query.message.edit_text(
            text = f'''<b>👋 Gʀᴇᴇᴛɪɴɢs , {query.from_user.mention} !  

🤖 I'ᴍ Mᴏʀᴇ Tʜᴀɴ Jᴜsᴛ A Bᴏᴛ! I'ᴍ A Cᴜsᴛᴏᴍ Cʀᴇᴀᴛɪᴏɴ Bʏ @Binge_Pirates , Aɴᴅ Mʏ Mɪssɪᴏɴ Is Tᴏ Dᴇʟɪᴠᴇʀ Mᴏᴠɪᴇs 🎬 Aɴᴅ Sᴇʀɪᴇs 📺 Rɪɢʜᴛ Tᴏ Yᴏᴜʀ Fɪɴɢᴇʀᴛɪᴘs, Sᴘᴇᴄɪᴀʟʟʏ Dᴇsɪɢɴᴇᴅ Fᴏʀ Yᴏᴜʀ Eɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ! 🍿📤

🌟 Pᴏᴡᴇʀᴇᴅ Bʏ ~ @Binge_Pirates</b>''',
            disable_web_page_preview = True,
            reply_markup = reply_markup
        )
    elif data == "premium":
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
            [InlineKeyboardButton("Cᴏɴᴛᴀᴄᴛ Fᴏʀ Qᴜᴇʀɪᴇs",url="https://telegram.me/Binge_Admin/3")]
        ])
        await query.message.reply_photo("https://mytoastlife.com/wp-content/uploads/2021/06/summer-classic-film-series.jpg",caption=text , reply_markup=reply_markup , quote=True)
        await query.answer()
    elif data.startswith('re'):
        code=data.split(maxsplit=1)[1]
        await query.answer(url=f'https://t.me/{client.me.username}?start={code}')