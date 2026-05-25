import os
from threading import Thread
from flask import Flask

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("TOKEN")

# ---------------- START ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "🟢 یک گیگ | 1.5 تون",
                callback_data="1g"
            )
        ],

        [
            InlineKeyboardButton(
                "🔵 دو گیگ | 3 تون",
                callback_data="2g"
            )
        ],

        [
            InlineKeyboardButton(
                "🟣 سه گیگ | 4.5 تون",
                callback_data="3g"
            )
        ],

        [
            InlineKeyboardButton(
                "🔴 نامحدود | 5 تون",
                callback_data="vip"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "💎 ابتدا یکی از پلن ها را انتخاب کنید",
        reply_markup=reply_markup
    )

# ---------------- BOT ----------------

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

# ---------------- FLASK ----------------

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running"

def run():
    flask_app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# ---------------- RUN ----------------

print("Bot Started...")

app.run_polling()
