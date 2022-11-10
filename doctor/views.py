from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from department.serializers import DepartmentSerializer
from myadmin.serializers import AppointmentSerializer
from patients.models import Appointment, Patient
from .models import Account, Doctor,Consulation
from .serializers import DoctorSerializer,ConsultSerializer,PatientSerializer
from account.serializers import AccountSerializer
from rest_framework import status,serializers
from rest_framework.response import Response
from department.models import Department
from pharmacy.models import Medicine
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import *


# Create your views here.
# class Doctor_Signup(APIView):

#     def post(self,request):
#         docsig = DoctorSerializer(data=request.data)

#         if docsig.is_valid():
#             docsig.save()
#             return Response(docsig.data,status = status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

class Doctor_Signup(APIView):

    def post(self,request):
        data=request.data
        dep_id = data["dep_id"]
        department = Department.objects.get(id=dep_id)


        user=Account.objects.create_user(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            phone_number=data["phone_number"],
            password=data["password"]

        )
        dep=Doctor.objects.create(department=department, user=user)
        dep.save()
        user.save()

        serializer = DoctorSerializer(dep)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Doctor_Signin(APIView):
    def post(self, request):

        data = request.data
        email = data["email"]
        password = data["password"]
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Wrong Credentials")
        if not user.is_doctor:
            raise serializers.ValidationError({"error": "You are not Authorized"})
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )

    

class AllDoc(generics.ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer


class UpdateDoctor(APIView):
  def get_object(self,id):
    try:
      return Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
      return Response(status=status.HTTP_400_BAD_REQUEST)
  
  def get(self,request,id):
    doctor_det=self.get_object(id)
    serializer=DoctorSerializer(doctor_det)
    return Response(serializer.data)
  
  def put(self,request,id):
    doctor_det=self.get_object(id)
    serializer=DoctorSerializer(doctor_det,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors)
  
  def delete(self,request,id):
    patient_obj=self.get_object(id)
    patient_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  


class DoctorConsultation(APIView):
   permission_classes = (IsAuthenticated,)

   def post(self,request):
      
      doctor=Doctor.objects.get(user=request.user)
      
      print(doctor.id)
      data=request.data 
      pat_id=data["pat_id"]
      patient=Patient.objects.get(id=pat_id)
      print(patient)
      # doc_id=data["doc_id"]
      # doc=Doctor.objects.get(id=doc_id)
      # print(doctor)
      conslt = Consulation.objects.create(
        
        
        doctor=doctor,
        patient=patient,
        symptoms=data["symptoms"],
        morning=data["morning"],
        afternoon=data["afternoon"],
        night=data["night"],
        days=data["days"]

      )
      # conslt.doctor=doctor.id
      # conslt.patient=patient.id,
      # conslt.medicine=medicine.id,
      conslt.save()
      print(conslt,'hiii')
      
      serializer = ConsultSerializer(conslt)

      return Response(serializer.data,status=status.HTTP_201_CREATED)



class ListPatients(APIView):

  permission_classes = (IsAuthenticated,)
  def get(self,request):
    doctor=request.user.id
    pat_list= Patient.objects.filter(user=Account.objects.get(id=doctor))
    print(pat_list)
    serializer= PatientSerializer(pat_list,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


    
# class ListPatients(APIView):
#     permission_classes = [isDoctor]

#     def get(self, request):
#         doctor = request.user
#         patient = user.patient_set.first()
#         patient_number = patient.class_number_id
#         student = AddStudent.objects.filter(class_number=patient_number)

#         serializer = StudentSerializer(
#             instance=student, many=True, context={"request": request}
#         )
#         return Response(serializer.data, status=status.HTTP_200_OK)


class ListAppointment(APIView):

  permission_classes = (IsAuthenticated,)
  def get(self,request):
    doctor=request.user.id
    apt_obj= Appointment.objects.filter(doctor=Doctor.objects.get(id=1))
    print(apt_obj)
    serializer= AppointmentSerializer(apt_obj,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)