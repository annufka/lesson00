import math
import string
import random
from datetime import datetime
import xlsxwriter

import requests
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.users.models import Profile, Currency
from app.users.serializer import ProfileSerializer


class GetUser(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user_id = request.user.id
        profile = Profile.objects.filter(user_id=user_id)[0]
        print(profile.id)
        snippet = self.get_object(pk=profile.id)
        serializer = ProfileSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PatchUserProfile(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def patch(self, request):
        user_id = request.user.id
        profile = Profile.objects.filter(user_id=user_id)[0]
        print(profile)
        object = self.get_object(profile.id)
        print(object.user.id)
        if request.user.id == object.user.id or request.user.is_superuser == True:
            serializer = ProfileSerializer(object, data=request.data,
                                             partial=True)  # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("No valid user")

class SendMail(APIView):
    def post(self, request, format=None):
        subject = request.data.get("subject")
        message = request.data.get("message")
        email = request.data.get("email")
        send_mail(
            subject,
            message,
            'brilchem@gmail.com',
            [email],
        )
        return Response("We send mail", status=status.HTTP_200_OK)

def password_generator(size=8, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class ResetPassword(APIView):
    def post(self, request, format=None):
        code = password_generator()
        print(code)
        try:
            user = User.objects.filter(email=request.data.get("email"))[0]
            print(user.id)
            profile = Profile.objects.filter(user_id=user.id).update(code=code)
            send_mail(
                "Reset Password",
                "Enter to http://127.0.0.1:8000/api/v1/users/activate/password/" + code + "Write your password",
                'brilchem@gmail.com',
                [request.data.get("email")],
            )
        except:
            pass
        return Response("Ok", status=status.HTTP_200_OK)

class ActivateNewPassword(APIView):
    def get(self, request, code, password, format=None):
        print(code)
        try:
            Profile.objects.filter(code=code).update(active=True)
            profile = Profile.objects.filter(code=code)[0]
            User.objects.filter(id=profile.id).update(password=make_password(password))
            Profile.objects.filter(code=code).update(code=0)
        except:
            pass
        return Response("Ok", status=status.HTTP_200_OK)


class GetCurrency(APIView):
    def post(self, request, format=None):
        responce = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")
        USD=responce.json()[0]
        print(USD.get("ccy"))
        new_currency = Currency(name=str(USD.get("ccy")) + "/" + str(USD.get("base_ccy")), value = str(USD.get("buy")), data_type=datetime.now())
        new_currency.save()
        return Response("OK", status=status.HTTP_201_CREATED)

class WriteToFile(APIView):
    def post(self, request, format=None):
        currency_list = []
        for item in Currency.objects.all():
            currency_list.append([item.id, item.name, round(float(item.value),2), str(item.data_type)])

        with xlsxwriter.Workbook('media/test.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, data in enumerate(currency_list):
                worksheet.write_row(row_num, 0, data)

        return Response("OK", status=status.HTTP_201_CREATED)

class PatchUserProfileToId(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def patch(self,request, id):
        user_id = id
        profile = Profile.objects.filter(user_id=user_id)[0]
        print(profile)
        object = self.get_object(profile.id)
        print(object.user.id)
        serializer = ProfileSerializer(object, data=request.data,
                                       partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#angular v.9> 