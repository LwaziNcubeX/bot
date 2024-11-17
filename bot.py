#!/usr/bin/env python3
"""
main
"""
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from plugins.commands.start import start_cmd
from utils.logger import logger

# Load environment variables
try:
    load_dotenv()
except FileNotFoundError:
    logger.info("No .env file found. Ignore if you are using a production bot")

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():
    """start main bot"""
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # COMMAND HANDLER
    app.add_handler(CommandHandler("start", start_cmd))

    # RUN
    app.run_polling()


if __name__ == "__main__":
    main()
