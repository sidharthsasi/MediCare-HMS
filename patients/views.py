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
from.models import *
from rest_framework import generics
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
        

    
class AllPatient(generics.ListAPIView):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer



class GetPatient(APIView):
  
  def get(self,request):
    patient_obj= Patient.objects.all()
    serializer= PatientSerializer(patient_obj,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

  def post(self,request):
    serializer=PatientSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class UpdateDelPatient(APIView):

  def get_object(self,id):
    try:
      return Patient.objects.get(id=id)
    except Patient.DoesNotExist:
      return Response(status=status.HTTP_400_BAD_REQUEST)
  
  def get(self,request,id):
    patient_det=self.get_object(id)
    serializer=PatientSerializer(patient_det)
    return Response(serializer.data)
  
  def put(self,request,id):
    patient_det=self.get_object(id)
    serializer=PatientSerializer(patient_det,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors)
  
  def delete(self,request,id):
    patient_det=self.get_object(id)
    patient_det.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

class Approve_Appointment(APIView):
   def post(self,request,id):
      apt=Appointment.objects.get(id=id)
      