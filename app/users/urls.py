from django.urls import path

from app.users.views import *

urlpatterns = [
    path('get/user/by/token/', GetUser.as_view()),
    path('send/mail/', SendMail.as_view()),
    path('reset/password/', ResetPassword.as_view()),
    path('activate/password/<int:code>/<str:password>/', ActivateNewPassword.as_view()),
    path('get/currency/', GetCurrency.as_view()),
    path('write/to/file/', WriteToFile.as_view()),
    path('patch/user/profile/', PatchUserProfile.as_view()),
    path('patch/user/profile/to/<int:id>/', PatchUserProfileToId.as_view()),
]