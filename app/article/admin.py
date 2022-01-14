from django.contrib import admin

from app.article.models import Category, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "title", "description", "price", "visible")

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)

