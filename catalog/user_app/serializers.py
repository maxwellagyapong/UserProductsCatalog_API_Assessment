from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True} 
        }
        
    def save(self, **kwargs):
        
        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')
        
        if password != password2:
            raise serializers.ValidationError({"Error": "P1 and P2 must be the same!"})
        
        if User.objects.filter(email=self.validated_data.get('email')).exists():
            raise serializers.ValidationError({"Error": "Email already exists!"})
        
        account = User(email=self.validated_data.get("email"), 
                       username=self.validated_data.get('username'),)
        account.set_password(password)
        
        account.save()
        
        return account
        
        
        