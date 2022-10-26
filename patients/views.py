from django.shortcuts import render
from rest_framework.views import APIView
from account.models import Account
from account.serializers import AccountSerializer, SignupSerializer
from rest_framework import status
from rest_framework.response import Response
from department.models import Department
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# Create your views here.
# class Signup(APIView):

#     def post(self,request):
#         sig = SignupSerializer(data=request.data)

#         if sig.is_valid():
#             sig.save()
#             return Response(sig.data,status = status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


class Patient_Signup(APIView):
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
    



class LogoutView(APIView):
    permission_classes = (IsAuthenticated)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        



class BookAppointment(APIView):
    serializer_class = AppointmentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=request.user.patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)