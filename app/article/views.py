from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.article.models import Category, Article
from app.article.pagination import ArticlePagination
from app.article.serializer import CategorySerializer, ArticleSmallSerializer, ArticleSerializer


class Test(APIView):

    def post(self, request, format=None):
        print("Hello, World!")
        number = int(request.data.get("number"))
        result = number + 1
        return Response(str(result), status=status.HTTP_201_CREATED)

class Calculate(APIView):

    def post(self, request, format=None):
        one_number = int(request.data.get("number_one"))
        two_number = int(request.data.get("number_two"))
        result = one_number+two_number
        return Response(str(result), status=status.HTTP_200_OK)

class CreateCategory(APIView):

    def post(self, request, format=None):
        name = str(request.data.get("name"))
        new_category = Category(name=name)
        new_category.save()
        return Response("OK", status=status.HTTP_200_OK)

class CreateCategoryMethodTwo(APIView):

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetListAllCategory(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class GetListAllArticles(generics.ListAPIView):
    serializer_class = ArticleSmallSerializer
    pagination_class = ArticlePagination

    def get_queryset(self):
        return Article.objects.all()

class ItemArticleViews(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializer(snippet)
        return Response(serializer.data)