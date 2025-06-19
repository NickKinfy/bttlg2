from flask import Flask
import telegram
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
import os

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running."

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    from flask import request
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return 'ok'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="👋 Welcome to KINFY Assistant!")

def not_now(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="No worries. Come back whenever you're ready 😊")

def info(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="We help you trade on Binance via API — no custody, no leverage, real results since Sept 2022.")

dp = Dispatcher(bot, None, workers=0)
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.regex("(?i)^not now$"), not_now))
dp.add_handler(MessageHandler(Filters.regex("(?i)^yes, tell me more$"), info))

if __name__ == '__main__':
    app.run(debug=True)
