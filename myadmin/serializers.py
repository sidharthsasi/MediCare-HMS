
from dataclasses import field
from rest_framework import serializers
from account.models import Account
from department.models import Department
from django.contrib.auth.hashers import make_password
from department.serializers import DepartmentSerializer
from doctor.models import Doctor
from patients.models import Appointment, Patient
from pharmacy.models import Medicine



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model= Department
        fields='__all__'


class DoctorSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    department = DepartmentSerializer()
    class Meta:
        model= Doctor
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}}


class PatientSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    class Meta:
        model= Patient
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Medicine
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    # patient=PatientSerializer()
    # doctor = DoctorSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'