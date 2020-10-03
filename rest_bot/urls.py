from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from app.views import UpdateBot, Check
from rest_bot import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('{}'.format(settings.BOT_TOKEN), csrf_exempt(UpdateBot.as_view()), name='update'),
    path('', csrf_exempt(Check.as_view()), name='check'),
]