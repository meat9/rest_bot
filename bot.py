import telebot
from telebot import types

from app.models import City, Category
from rest_bot import settings

bot = telebot.TeleBot(settings.BOT_TOKEN)


def makeKeyboard(btn_names, row_width=2):
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    btn_names = [types.InlineKeyboardButton(text=name, callback_data=name) for name in btn_names]

    keyboard.add(*btn_names)
    return keyboard


@bot.message_handler(commands=['start'])
def start(message):
    # bot.delete_message(message.chat.id, message.message_id)
    text = 'Привет!🤗\nЯ помогу тебе выбрать ресторан.\nВ каком городе ищем?'

    cities = City.objects.all()
    cities_for_btns = [city.name for city in cities]

    keyboard = makeKeyboard(cities_for_btns)

    bot.send_message(message.chat.id, text=text, reply_markup=keyboard, parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'Москва' or call.data == 'Санкт-Петербург':
        show_categories(call)
    if call.data == 'Сменить город':
        start(call.message)


def show_categories(call):
    text = 'Отлично! Выбери подборку, куда ты хочешь сходить.'

    categories = Category.objects.filter(restaurant__cities__name=call.data).distinct()

    btn_info = [category.name for category in categories]
    btn_info.append('Показать рестораны рядом')
    btn_info.append('Сменить город')

    keyboard = makeKeyboard(btn_info, row_width=1)

    bot.edit_message_text(chat_id=call.message.chat.id,
                          text="Отлично! Выбери подборку, куда ты хочешь сходить.",
                          message_id=call.message.message_id,
                          reply_markup=keyboard,
                          parse_mode='HTML')




# Вебхук бота
bot.remove_webhook()
bot.set_webhook(url=f"{settings.DOMAIN}/{settings.BOT_TOKEN}")
