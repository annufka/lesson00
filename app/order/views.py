from rest_framework.response import Response
from rest_framework.views import APIView

from app.order.serializer import OrderSerializer, ElementOrderSerializer
from rest_framework import status


class CreateOrder(APIView):

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if str(request.user) != 'AnonymousUser':
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateElementOrder(APIView):

    def post(self, request, format=None):
        serializer = ElementOrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

