from django.shortcuts import render
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer, SignupSerializer
from rest_framework import status
from rest_framework.response import Response
from department.models import Department

# Create your views here.
# class Signup(APIView):

#     def post(self,request):
#         sig = SignupSerializer(data=request.data)

#         if sig.is_valid():
#             sig.save()
#             return Response(sig.data,status = status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


class Signup(APIView):
    def post(self,request):
        data=request.data


        user=Account.objects.create_user(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            phone_number=data["phone_number"],
            
            password=data["password"]


        )
        user.is_patient=data["is_patient"]
        print(data["is_patient"])
        user.save()

        serializer = AccountSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)