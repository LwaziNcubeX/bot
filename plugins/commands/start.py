#!/usr/bin/env python3
"""
start command
"""
from telegram import Update, ReplyKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

keyboard = [
        ["😭 Help", "👤 Account"],
        ["⚙️ Settings", "🌟 About Us"],
    ]

start_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start command
    """
    
    await update.message.reply_text(
        f"Hi, send me a direct download link and I will upload the contents to Telegram.\n\n"
        f"If you are new to this bot, please press <b>/Help</b>.\n",
        reply_markup=start_markup,
        parse_mode=ParseMode.HTML
    )
