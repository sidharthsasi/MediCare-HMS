from rest_framework import serializers
from account.models import Account
from django.contrib.auth.hashers import make_password
from.models import Appointment, Patient
from patients.models import Appointment
from department.serializers import DepartmentSerializer




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



class SignupSerializer(serializers.ModelSerializer):

    class Meta:

        model= Account
        fields = '__all__'
        # validate_password = make_password
    
        # def create(self, validated_data):
        #     user = Account.objects.create(
        #         username=validated_data["username"],
        #         email=validated_data["email"],
        #         first_name=validated_data["first_name"],
        #         last_name=validated_data["last_name"],
        #         phone_number=validated_data["phone_number"],
        #         is_patient=validated_data["is_patient"],
        #         password = make_password(validated_data['password'])
        #     )
            
        #     user.save()
        #     return user

        # def validate(self,validated_data):

        #     username = validated_data.get('username')
        #     email = validated_data.get('email')
        #     phone_number = validated_data.get('phone_number')
            

        #     if Account.objects.filter(username=username).exists():
        #         raise serializers.ValidationError({'username':('username already exists')})

        #     if Account.objects.filter(email=email).exists():
        #         raise serializers.ValidationError({'email':('email already exists')})

        #     if Account.objects.filter(phone_number=phone_number).exists():
        #         raise serializers.ValidationError({'phone_number':('phone number is already exists')})
            
        #     return super().validate(validated_data)



class AppointmentSerializer(serializers.ModelSerializer):
    # user = AccountSerializer()
    class Meta:
        model =Appointment
        fields='__all__'


class PatientSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    class Meta:
        model= Patient
        fields = '__all__'
