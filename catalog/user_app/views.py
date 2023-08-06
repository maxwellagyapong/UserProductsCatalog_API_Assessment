from .models import * 
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, logout
from django.contrib import auth
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tasks import send_password_reset_email
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse

User = get_user_model()


class RegistrationView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [AllowAny]

	def create(self, request):
		data = UserSerializer(data=request.data)
		data.is_valid(raise_exception=True)
		validated_data = data.data
		email = validated_data["email"]
		
		if User.objects.filter(email=email).exists():
			return Response({
				"status": status.HTTP_500_INTERNAL_SERVER_ERROR,
				"message": "Email already exist!"
			}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		else:
			try:
				password = request.data["password"]
				password2 = request.data["password2"]
				if "@" not in email or ".com" not in email:
					return Response({
						"status": status.HTTP_400_BAD_REQUEST,
						"message": "Invalid email address!",
					}, status=status.HTTP_400_BAD_REQUEST)
     
				elif len(password) < 8:
					return Response({
						"status": status.HTTP_400_BAD_REQUEST,
						"message": "Password must contain at least 8 characters!",
					}, status=status.HTTP_400_BAD_REQUEST)
     
				elif password != password2:
					return Response({
						"status": status.HTTP_400_BAD_REQUEST,
						"message": "password and password2 must be the same!",
					}, status=status.HTTP_400_BAD_REQUEST)					
				else:
					
					user = User.objects.create(
							first_name=validated_data["first_name"],
                            last_name=validated_data["last_name"],
							email=email
						)
					user.set_password(password)
					# user.userId = generate_userId()
					user.save()
										
					return Response({
                        "message": "Account registration was successful.",
						"status": status.HTTP_201_CREATED,
						"email": user.email,
						
					}, status=status.HTTP_201_CREATED)
					

			except Exception as e:
				return Response({
					"status": status.HTTP_500_INTERNAL_SERVER_ERROR,
					"message": "Something went wrong. " + str(e),
				}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(generics.GenericAPIView):
	serializer_class = UserLoginSerializer
	permission_classes = [AllowAny]

	def post(self, request):
		data = UserLoginSerializer(data=request.data)
		data.is_valid(raise_exception=True)
		validated_data = data.data 

		email = validated_data["email"]
		password = validated_data["password"]
		user = auth.authenticate(email=email, password=password)
		if user:
			token = RefreshToken.for_user(user).access_token
	
			data = {
                'message': 'Login Successful',
				'status': status.HTTP_200_OK,
				'token': str(token),
			}
			return Response(data, status=status.HTTP_200_OK)
			
		return Response({
			'status': status.HTTP_404_NOT_FOUND,
			'message': 'Please enter the correct email and password!'
		}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		logout(request)
		return Response({
			"status":status.HTTP_200_OK,
			"message":"Logged out"
			}, status=status.HTTP_200_OK)


class PasswordResetRequestView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        
        reset_url = "127.0.0.1/api/account/reset-password/"

        if user:
            token = PasswordResetTokenGenerator().make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = reverse('password-reset-confirm', args=[uid, token])
            send_password_reset_email.delay(user.email, reset_url)  # Send email asynchronously
            return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class PasswordResetConfirmView(APIView):
		permission_classes = [AllowAny]

		def post(self, request, uidb64, token):

			try:
				uid = force_str(urlsafe_base64_decode(uidb64))
				user = User.objects.get(pk=uid)
			except (TypeError, ValueError, OverflowError, User.DoesNotExist):
				user = None

			if user is not None and PasswordResetTokenGenerator().check_token(user, token):
				serializer = PasswordResetConfirmSerializer(data=request.data)
				serializer.is_valid(raise_exception=True)
				
				new_password = serializer.validated_data['new_password']
				user.set_password(new_password)
				user.save()
				
				return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)

			return Response({'error': 'Invalid reset link'}, status=status.HTTP_400_BAD_REQUEST)
