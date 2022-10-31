from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics
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