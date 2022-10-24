from rest_framework import serializers
from .models import Account


class SignupSerializer(serializers.ModelSerializer):

    class Meta:

        model= Account
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}}

    
        def create(self,validated_data):
            
            user = Account.objects.create_user(**validated_data)
            return user


        def validate(self,validated_data):

            username = validated_data.get('username')
            email = validated_data.get('email')
            phone_number = validated_data.get('phone_number')


            if Account.objects.filter(username=username).exists():
                raise serializers.ValidationError({'username':('username already exists')})

            if Account.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email':('email already exists')})

            if Account.objects.filter(phone_number=phone_number).exists():
                raise serializers.ValidationError({'phone_number':('phone number is already exists')})


            return super().validate(validated_data)


            
