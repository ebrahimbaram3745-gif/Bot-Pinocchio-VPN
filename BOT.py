import os
from threading import Thread
from flask import Flask

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
    ButtonStyle
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("TOKEN")

dp = Dispatcher()


emojis = {
    "hello": ("5440431182602842059", "👋"),
    "start-eye": ("5253800186278325174", "🤩"),
    "fire": ("5463154755054349837", "🔥"),
}


@dp.message()
async def start(message: Message): ...
markup = InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(
                text=" آبی ممد",
                callback_data="BLUE_BTN",
                style=ButtonStyle.PRIMARY
            )
        ],

        [
            InlineKeyboardButton(
                text=" قرمز ممد",
                callback_data="RED",
                style=ButtonStyle.DANGER
            )
        ],

    ]
)
await message.answer(
    text="Sample Text",
    reply_markup=markup
)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    await dp.start_polling(bot)
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

if __name__ == "__main__":
    asyncio.run(main())
