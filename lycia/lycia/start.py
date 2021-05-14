from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
I am 🦊 Fox X AI Bot, An Intelligent ChatBot
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("🦊 Fox X AI Bot", switch_inline_query_current_chat="lycia "), InlineKeyboardButton("Github", url = "https://github.com/Red-Aura/Lyciachatbot")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
