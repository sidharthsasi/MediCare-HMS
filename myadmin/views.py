from django.shortcuts import render
from rest_framework.views import APIView

from patients.models import Appointment
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class AdminDashboard(APIView):
    pass 


class AllDoc(generics.ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

class AllDepartment(generics.ListAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer


class AllPatient(generics.ListAPIView):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer


class AllAppointment(generics.ListAPIView):
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer



class AddDepartment(APIView):

    def post(self,request):
        dep=DepartmentSerializer(data=request.data)
        if dep.is_valid():
            dep.save()
            return Response(dep.data,status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    


class AddDoctor(APIView):

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



  
class AddMedicine(APIView):

  def post(self,request):
      med=MedicineSerializer(data=request.data)
      if med.is_valid():
          med.save()
          return Response(med.data,status = status.HTTP_201_CREATED)
      return Response(status=status.HTTP_400_BAD_REQUEST)
    