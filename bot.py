import os
from telegram import Bot

def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError("BOT_TOKEN or CHAT_ID missing")

    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text="Test successful ✅")

if __name__ == "__main__":
    main()
