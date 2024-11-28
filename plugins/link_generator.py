from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import *
from helper import *
from itertools import count as ctr

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client, message):
    for i in ctr():
        try:
            first_message = await client.ask(text = "<b>Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link</b>" , reply_to_message_id = message.id ,chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("<b>❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel</b>", quote = True)
            continue
    while True:
        try:
            second_message = await client.ask(text = "<b>Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link</b>", reply_to_message_id = message.id , chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("<b>❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel</b>", quote = True)
            continue
    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.me.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Direct URL", url=link)]])
    await second_message.reply_text(f"<b>Here is your link\n\n{link}</b>", quote=True, reply_markup=reply_markup)

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client, message):
    for i in ctr():
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", reply_to_message_id = message.id , chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.me.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=link)]])
    await channel_message.reply_text(f"<b>Here is your link\n\n{link}</b>", quote=True, reply_markup=reply_markup)