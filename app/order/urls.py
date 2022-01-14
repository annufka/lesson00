from django.urls import path

from app.order.views import CreateOrder, CreateElementOrder

urlpatterns = [
    path('create/order/', CreateOrder.as_view()),
    path('create/element/order/', CreateElementOrder.as_view()),
]