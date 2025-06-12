import telebot
from telebot.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot("7876485835:AAGz0RqhyobWjAi7g7KHl8r8mn-2hVwhb2E")

@bot.message_handler(commands=["start"])
def start(msg):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("📊 Открыть Market", web_app=WebAppInfo(url="https://yourapp.up.railway.app")))
    bot.send_message(msg.chat.id, "Добро пожаловать! Нажми кнопку ниже, чтобы открыть маркет:", reply_markup=kb)

bot.polling()
