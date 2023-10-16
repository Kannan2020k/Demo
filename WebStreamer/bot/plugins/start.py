from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram import filters
from WebStreamer.utils.Translation import Language, BUTTON
from pyrogram.enums.parse_mode import ParseMode

@StreamBot.on_message(filters.command(['start','help']) & filters.private)
async def start(b, m):
    lang = Language(m)
    await m.reply_text(
        text=lang.START_TEXT.format(m.from_user.mention),
        parse_mode=ParseMode.HTML,
        reply_markup=BUTTON.START_BUTTONS
        )


