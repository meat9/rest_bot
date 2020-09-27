from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model
from gsheets import mixins

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")


class Test(mixins.SheetSyncableMixin, models.Model):
    spreadsheet_id = '1Z41RhS77kYyglpapnISlQ6dpTg1C8ouqea_JiDIV0Hg'
    sheet_name = 'Лист1'

    guid = models.CharField(primary_key=True, max_length=255, default=uuid4)

    test_field = models.CharField(max_length=127)


    def __str__(self):
        return f'{self.test_field})'
