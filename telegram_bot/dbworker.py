import redis

from rest_bot import settings
from telegram_bot import config

db = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

# Пытаемся узнать из базы «состояние» пользователя
def get_chosen_city(user_id):
    try:
        return db[user_id]
    except KeyError:  # Если такого ключа почему-то не оказалось
        return 'You have to choose city'  # значение по умолчанию - начало диалога

# Сохраняем текущее «состояние» пользователя в нашу базу
def save_users_city(user_id, city):
    try:
        db[user_id] = city
        return True
    except:
        # тут желательно как-то обработать ситуацию
        return False
