from django.urls import path

from app.shop.views import GetAllProducts

urlpatterns = [
    path('get/list/all/products/', GetAllProducts.as_view()),
]