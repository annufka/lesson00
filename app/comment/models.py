from django.contrib.auth.models import User
from django.db import models
from pytz import unicode


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return unicode(str(self.name))

#null=true, blank=true - не обязательно к заполнению
class Comment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return unicode(str(self.text))

