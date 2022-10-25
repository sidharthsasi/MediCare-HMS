from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Department
        fields='__all__'
