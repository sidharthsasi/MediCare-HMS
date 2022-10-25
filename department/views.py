from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from .models import Department
from rest_framework import status
from rest_framework.response import Response


# Create your views here.


class AddDepartment(APIView):

    def post(self,request):
        dep=DepartmentSerializer(data=request.data)
        if dep.is_valid():
            dep.save()
            return Response(dep.data,status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)