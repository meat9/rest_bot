from django.contrib import admin

from app.models import Restaurant, City, Category, Options


class RestaurantAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class OptionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Options, OptionsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(City, CityAdmin)
