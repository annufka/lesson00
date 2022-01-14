from django.contrib.auth.models import User
from django.db import models
from pytz import unicode

from app.shop.models import Product


class Status(models.Model):
    name_status = models.CharField(max_length=20)

    def __str__(self):
        return unicode(str(self.name_status))

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    summ = models.FloatField(default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return unicode(str(self.name))

class ElementOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return unicode(str(self.product))