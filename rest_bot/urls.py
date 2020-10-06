from django.contrib import admin
from django.urls import path, include
import gsheets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gsheets.urls')),
]
