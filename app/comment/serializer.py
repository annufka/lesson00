from rest_framework import serializers

from app.comment.models import Category, Comment


class CategoryCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    category = CategoryCommentsSerializer(read_only=True, many=False)

    class Meta:
        model = Comment
        fields = "__all__"

class CreateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
