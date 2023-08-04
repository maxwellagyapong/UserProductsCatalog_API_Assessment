from . import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(max_length=200)
	last_name = serializers.CharField(max_length=200)
	password = serializers.CharField(style={'input_type': 'password'},
		max_length=65, min_length=8, write_only=True)
	email = serializers.EmailField(max_length=255, min_length=4)
 
	class Meta:
		model= models.User
		fields = ['first_name', 'last_name', 'email', 'password']
		extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=65, min_length=8)
	email = serializers.EmailField(max_length=255, min_length=4)

	class Meta:
		model = models.User
		fields = ["email", "password"]