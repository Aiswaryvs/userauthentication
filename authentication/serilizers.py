from rest_framework import serializers
from authentication.models import *




class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","mobilephone","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

