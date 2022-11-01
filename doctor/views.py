from django.shortcuts import render
from rest_framework.views import APIView

from department.serializers import DepartmentSerializer
from patients.models import Patient
from .models import Account, Doctor
from .serializers import DoctorSerializer
from account.serializers import AccountSerializer
from rest_framework import status
from rest_framework.response import Response
from department.models import Department
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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
  


class Consultation(APIView):
   permission_classes = (IsAuthenticated,)

   def post(self,request):
      user=request.user
      data=request.data 
      pat_id=data["pat_id"]
      patient=Patient.objects.get(id=pat_id)


      