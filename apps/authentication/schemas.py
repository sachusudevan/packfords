
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterPostSchema(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']


class RegisterSchema(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username',
                  'first_name', 'last_name', 'is_active', 'is_verified', 'is_superuser','date_joined']


class LoginPostSchema(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class LoginSchema(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username',
                  'first_name', 'last_name', 'is_active',  'is_superuser','date_joined']


class UsersSchema(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username',
                  'first_name', 'last_name', 'is_active', 'is_superuser','date_joined']

