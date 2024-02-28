# This file is a part of TG-FileStreamBot

import asyncio
from WebStreamer.bot import StreamBot
from WebStreamer.utils.file_properties import gen_link
from WebStreamer.vars import Var
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums.parse_mode import ParseMode
from WebStreamer.utils.dulink import get_shortlink

#zmain_chat = Var.AUTH_CHANNEL

@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def private_receive_handler(c: Client, m: Message):
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        reply_markup, Stream_Text, stream_link = await gen_link(m=m, log_msg=log_msg, from_channel=False)
        await log_msg.reply_text(text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Dᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN, quote=True)

        await m.reply_text(
            text=Stream_Text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.value)}s")
        await asyncio.sleep(e.value)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.value)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

@StreamBot.on_message(filters.channel & (filters.document | filters.video), group=-1)
async def channel_receive_handler(bot, broadcast: Message):
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        return
    if int(broadcast.chat.id) == int(Var.BIN_CHANNEL):
        return 
    media = broadcast.document or broadcast.video or broadcast.audio

    if (broadcast.document or broadcast.video or broadcast.audio): 
        if broadcast.caption:                        
           file_caption = f"{broadcast.caption}"                
        else:
           file_caption = ""
    file_caption = file_caption.replace("", "")
    file_caption = file_caption.replace("", "")
    file_caption = file_caption.replace("", "")
    file_caption = file_caption.replace("", "")
    file_caption = file_caption.replace("", "")
    file_caption = file_caption.replace("", "")
    file_caption = file_caption.replace("", "")
    file_caption = file_caption.replace("", "")
                         
        #return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        edit_message_caption, Stream_Text, stream_link = await gen_link(m=broadcast, log_msg=log_msg, from_channel=True)
        await log_msg.reply_text(
            text=f"**Cʜᴀɴɴᴇʟ Nᴀᴍᴇ:** `{broadcast.chat.title}`\n**Cʜᴀɴɴᴇʟ ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** {stream_link}",
            # text=f"**Cʜᴀɴɴᴇʟ Nᴀᴍᴇ:** `{broadcast.chat.title}`\n**Cʜᴀɴɴᴇʟ ID:** `{broadcast.chat.id}`\n**Rᴇǫᴜᴇsᴛ ᴜʀʟ:** https://t.me/FxStreamBot?start=msgid_{str(log_msg.id)}",
            quote=True,
            parse_mode=ParseMode.MARKDOWN
        )
        await bot.edit_message_caption(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,            
            caption = Var.CUSTOM_FILE_CAPTION.format(file_name ='' if file_caption is None else file_caption,
                                                     short_link ='' if stream_link is None else stream_link,
                                                     main_chat ='' if Var.AUTH_CHANNEL is None else Var.AUTH_CHANNEL)

            )
    except FloodWait as w:
        print(f"Sleeping for {str(w.value)}s")
        await asyncio.sleep(w.value)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(w.value)}s from {broadcast.chat.title}\n\n**Cʜᴀɴɴᴇʟ ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ᴇʀʀᴏʀ_ᴛʀᴀᴄᴇʙᴀᴄᴋ:** `{e}`", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ: {e}")

# Feature is Dead no New Update for Stream Link on Group
@StreamBot.on_message(filters.group & (filters.document | filters.video | filters.audio), group=4)
async def private_receive_handler(c: Client, m: Message):
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        reply_markup, Stream_Text, stream_link = await gen_link(m=m, log_msg=log_msg, from_channel=True)
        await log_msg.reply_text(text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.chat.first_name}](tg://user?id={m.chat.id})\n**Group ɪᴅ :** `{m.from_user.id}`\n**Dᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN, quote=True)

        await m.reply_text(
            text=Stream_Text,
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
    except FloodWait as e:
        print(f"Sleeping for {str(e.value)}s")
        await asyncio.sleep(e.value)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.value)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

