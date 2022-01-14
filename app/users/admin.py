from django.contrib import admin

from app.users.models import Profile, Currency


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user",  "code", "active"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Currency)