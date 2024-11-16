#!/usr/bin/env python3
"""
start command
"""
from telegram import Update, ReplyKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from models.user import User

keyboard = [
        ["😭 Help", "👤 Account"],
        ["⚙️ Settings", "🌟 About Us"],
    ]

start_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start command
    """
    user = User(update)  # Initialize User object with Update object

    new_data = {"name": user.name, "username": user.username}
    await user.check(new_data)

    await update.message.reply_text(
        f"Hi, send me a direct download link and I will upload the contents to Telegram.\n\n"
        f"If you are new to this bot, please press <b>/Help</b>.\n",
        reply_markup=start_markup,
        parse_mode=ParseMode.HTML
    )
