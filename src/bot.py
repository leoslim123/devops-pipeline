import telebot
import os
import sys
import datetime

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    print("Ошибка: переменная окружения BOT_TOKEN не задана")
    sys.exit(1)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для уведомлений о pipeline.")
    bot.send_message(message.chat.id, "Используй /help чтобы посмотреть команды")


@bot.message_handler(commands=['help'])
def cmd_help(message):
    txt = "Доступные команды:\n"
    txt += "/start - запуск бота\n"
    txt += "/help - справка\n"
    txt += "/status - статус бота\n"
    txt += "/chatid - узнать ID чата"
    bot.send_message(message.chat.id, txt)


@bot.message_handler(commands=['status'])
def cmd_status(message):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(message.chat.id, f"Бот работает\nВремя сервера: {now}")


@bot.message_handler(commands=['chatid'])
def cmd_chatid(message):
    bot.send_message(message.chat.id, f"Chat ID: {message.chat.id}")


@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, "Неизвестная команда. Напиши /help")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()


