from django.urls import path

from app.comment.views import GetListAllComments, CreateComment, Test, PatchCommentViews

urlpatterns = [
    path('get/list/all/comments/', GetListAllComments.as_view()),
    path('create/comment/', CreateComment.as_view()),
    path('test/', Test.as_view()),
    path('patch/comment/<int:pk>/', PatchCommentViews.as_view()),
    ]