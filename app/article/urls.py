from django.urls import path, include

from app.article.views import *

urlpatterns = [
    path('test/', Test.as_view()),
    path('calculate/', Calculate.as_view()),
    path('create/category/', CreateCategory.as_view()),
    path('create/category/two/', CreateCategoryMethodTwo.as_view()),
    path('get/list/all/category/', GetListAllCategory.as_view()),
    path('get/list/all/articles/', GetListAllArticles.as_view()),
    path('get/article/item/<int:pk>/', ItemArticleViews.as_view()),
]