from rest_framework import serializers

from department.serializers import DepartmentSerializer
from .models import  Doctor,Consulation,Record
from django.contrib.auth.hashers import make_password
from account.serializers import AccountSerializer
from patients.models import Patient

class DoctorSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    department = DepartmentSerializer()
    class Meta:
        model= Doctor
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}}
        # validate_password = make_password
    
        # def create(self, validated_data):
        #     user = Doctor.objects.create(
        #         username=validated_data["username"],
        #         email=validated_data["email"],
        #         first_name=validated_data["first_name"],
        #         last_name=validated_data["last_name"],
        #         phone_number=validated_data["phone_number"],
        #         is_doctor=validated_data["is_doctor"],
                
        #     )
        #     user.set_password(validated_data["password"])
        #     user.save()
        #     return user

        # def validate(self,validated_data):

        #     username = validated_data.get('username')
        #     email = validated_data.get('email')
        #     phone_number = validated_data.get('phone_number')
            

        #     if Doctor.objects.filter(username=username).exists():
        #         raise serializers.ValidationError({'username':('username already exists')})

        #     if Doctor.objects.filter(email=email).exists():
        #         raise serializers.ValidationError({'email':('email already exists')})

        #     if Doctor.objects.filter(phone_number=phone_number).exists():
        #         raise serializers.ValidationError({'phone_number':('phone number is already exists')})
            
        #     return super().validate(validated_data)


            
class ConsultSerializer(serializers.ModelSerializer):
     user = AccountSerializer()
     class Meta:
        model=Consulation
        fields='__all__'


class PatientSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    class Meta:
        model= Patient
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
   
    
    class Meta:
        model = Record
        fields = ("patient", "file")