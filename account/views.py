from django.shortcuts import render
from rest_framework.views import APIView
from .models import Account
from .serializers import SignupSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class Signup(APIView):

    def post(self,request):
        sig = SignupSerializer(data=request.data)

        if sig.is_valid():
            sig.save()
            return Response(sig.data,status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
