import telebot
from telebot import types

from app.models import City
from rest_bot import settings

bot = telebot.TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.delete_message(message.chat.id, message.message_id)
    text = 'Привет!🤗\nЯ помогу тебе выбрать ресторан.\nВ каком городе ищем?'

    keyboard = types.InlineKeyboardMarkup()

    cities = City.objects.all()

    key_begin = types.InlineKeyboardButton(text='🖊️ Начать', callback_data='begin')
    keyboard.add(*[types.InlineKeyboardButton(text=city.name, callback_data=city.name) for city in cities])


    bot.send_message(message.chat.id, text=text, reply_markup=keyboard, parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: True)
def show_categories(call):
    if call.data == 'Москва':
        bot.send_message(call.message.chat.id, 'Бордюр')
    elif call.data == 'Санкт-Петербург':
        bot.send_message(call.message.chat.id, 'Поребрик')


# Вебхук бота
bot.remove_webhook()
bot.set_webhook(url=f"{settings.DOMAIN}/{settings.BOT_TOKEN}")