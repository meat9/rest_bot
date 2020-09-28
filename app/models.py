from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model


class City(models.Model):
    """Модель, описывающая город"""
    name = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    """Модель, описывающая категорию ресторана
    (например, 'быстро и не дорого' или 'приятно провести время')"""
    name = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.name}'


class Options(models.Model):
    """Модель, описывающая дополнительные опции ресторана
    (например, 'веранда' или 'дог-френдли')"""
    name = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.name}'


class Restaurant(models.Model):
    """Модель, описывающая ресторан"""
    name = models.CharField(max_length=55)
    short_description = models.CharField(max_length=250)
    address = models.TextField()
    full_description = models.TextField()
    cities = models.ManyToManyField(City)
    categories = models.ManyToManyField(Category)
    google_map_link = models.CharField(max_length=250)
    options = models.ManyToManyField(Options)


    def __str__(self):
        return f'{self.name}'