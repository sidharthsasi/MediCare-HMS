from django.shortcuts import render
from rest_framework.views import APIView

from department.serializers import DepartmentSerializer
from .models import Account, Doctor
from .serializers import DoctorSerializer
from account.serializers import AccountSerializer
from rest_framework import status
from rest_framework.response import Response
from department.models import Department
from rest_framework import generics

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