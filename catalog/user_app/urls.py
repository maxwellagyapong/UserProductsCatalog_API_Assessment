from django.urls import path
from .views import (RegistrationView, LoginView, 
                    LogoutView, PasswordResetRequestView, PasswordResetConfirmView)

urlpatterns = [
	path('register/', RegistrationView.as_view(), name='register'),
	path('login/', LoginView.as_view(), name="login"),
	path('logout/', LogoutView.as_view(), name="logout"),
	path('reset-password/', PasswordResetRequestView.as_view(), name="password-reset"),
	path('reset-password-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
