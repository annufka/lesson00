from django.contrib import admin
from app.comment.models import Category, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "category", "user")

admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)