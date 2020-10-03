import telebot
from django.http import HttpResponse
from django.views.generic.base import View

from telebot import types

from bot import bot

update_id = None


class Check(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Бот запущен и работает.\n <a href='/admin'>Перейти в админку</a>")

class UpdateBot(View):
    def post(self, request):
        global update_id
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        if update_id != update.update_id:
            bot.process_new_updates([update])
            update_id = update.update_id
        return HttpResponse(status=200)


