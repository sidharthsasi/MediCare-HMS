from django.shortcuts import render
from rest_framework.views import APIView
from account.models import Account
from account.serializers import AccountSerializer, SignupSerializer
from rest_framework import status
from rest_framework.response import Response
from department.models import Department
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from doctor.models import Doctor
from .serializers import *


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
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
        pat=Patient.objects.create(
            user=user,
            date_of_birth=data["date_of_birth"],
            address=data["address"],
            blood_group=data["blood_group"]
            )
        pat.save()
        user.save()

        serializer = PatientSerializer(pat)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    



class LogoutView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        



class BookAppointment(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user=request.user
        print(user)
        data=request.data
        doc_id=data["doc_id"]
        doctor=Doctor.objects.get(id=doc_id)


        apt=Appointment.objects.create(

            
            user=user,
            doctor=doctor,
            age=data["age"],
            date=data["date"],
            time=data["time"]
        )

        apt.save()
        serializer = AppointmentSerializer(apt)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        