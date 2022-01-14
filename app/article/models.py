from django.db import models
from pytz import unicode


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return unicode(str(self.name))

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()
    price = models.FloatField(default=0)
    index = models.IntegerField(default=1111)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return unicode(str(self.title))
