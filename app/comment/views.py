from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.comment.models import Comment
from app.comment.serializer import CategoryCommentsSerializer, CommentSerializer, CreateCommentSerializer


class GetListAllComments(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class CreateComment(APIView):

    def post(self, request, format=None):
        serializer = CreateCommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=request.user.id)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Test(APIView):

    def post(self, request, format=None):
        print(request.user)
        return Response("Hello", status=status.HTTP_201_CREATED)

class PatchCommentViews(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommentSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk):
        user_id = request.user.id
        user = User.objects.filter(id=user_id)[0]
        print(user.id)
        object = self.get_object(pk)
        print(object.user.id)
        if request.user.id == object.user.id or request.user.is_superuser == True:
            serializer = CreateCommentSerializer(object, data=request.data,
                                             partial=True)  # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No valid user")

    def post(self, request, pk, format=None):
        print(request.user)
        return Response("Hello", status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        if request.user.id == snippet.user.id or request.user.is_superuser == True:
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("No valid user")

