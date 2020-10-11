# import telebot
# from django.db.models import Q
# from telebot import types
#
# from app.models import City, Category, Restaurant
# from rest_bot import settings
# from telegram_bot import dbworker, config
#
# bot = telebot.TeleBot(settings.BOT_TOKEN)
#
#
# def makeKeyboard(btn_names, callback_name=None, row_width=2):
#     keyboard = types.InlineKeyboardMarkup(row_width=row_width)
#
#     keyboard.add(
#         *[types.InlineKeyboardButton(text=name, callback_data=f'{name}_{callback_name}') for name in btn_names])
#     return keyboard
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     text = 'Привет!🤗\nЯ помогу тебе выбрать ресторан.\nВ каком городе ищем?'
#
#     cities = City.objects.all()
#     cities_for_btns = {'city': [city.name for city in cities]}
#
#     keyboard = makeKeyboard(btn_names=cities_for_btns['city'], callback_name='list_of_categories')
#     bot.send_message(message.chat.id, text=text, reply_markup=keyboard, parse_mode='HTML')
#
#
#
#
# @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_NAME.value)
# @bot.callback_query_handler(func=lambda call: 'list_of_categories' in call.data)
# dbworker.save_users_city(message.from_user.id, city)
#
#
#
# # Вебхук бота
# bot.remove_webhook()
# bot.set_webhook(url=f"{settings.DOMAIN}/{settings.BOT_TOKEN}")
