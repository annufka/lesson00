from rest_framework import serializers

from app.article.models import Category, Article


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id","name"]
        #fields = '__all__'

class ArticleSmallSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    class Meta:
        model = Article
        fields = ["id", "category", "title", "description", "visible"]

        """
        title = models.CharField(max_length=200)
        description = models.CharField(max_length=200, null=True, blank=True)
        text = models.TextField()
        price = models.FloatField(default=0)
        index = models.IntegerField(default=1111)
        visible
        """

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    class Meta:
        model = Article
        fields = "__all__"