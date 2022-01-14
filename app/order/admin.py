from django.contrib import admin

from app.order.models import *

admin.site.register(Status)
admin.site.register(ElementOrder)
admin.site.register(Order)

