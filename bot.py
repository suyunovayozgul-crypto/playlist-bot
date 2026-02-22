import telebot
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(8318806269:AAHN5zzALREJRiwU4j9IiEsCip4OkcyOGQM)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is working ✅")

bot.infinity_polling()
