from app.order.models import Order, ElementOrder
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class ElementOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElementOrder
        fields = '__all__'