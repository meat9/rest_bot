from django.contrib import admin
from .models import Post, Test


class PostAdmin(admin.ModelAdmin):
    # поля, отображаемые в админке
    list_display = ("pk", "text", "pub_date", "author") 
    # поиск по тексту постов
    search_fields = ("text",) 
    # фильтрация по дате
    list_filter = ("pub_date",) 
    empty_value_display = "-пусто-" # где пусто - там будет эта строка (для всех колонок)

admin.site.register(Post, PostAdmin)

class TestAdmin(admin.ModelAdmin):
    list_display = ("guid", "test_field") 
    search_fields = ("text",) 
    empty_value_display = "-пусто-"  
admin.site.register(Test, TestAdmin)


