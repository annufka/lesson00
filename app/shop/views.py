from rest_framework import generics

from app.shop.models import Product
from app.shop.serializer import ProductSerializer


class GetAllProducts(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()
