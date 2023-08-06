from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, PasswordResetView

urlpatterns = [
	path('register/', RegistrationView.as_view(), name='register'),
	path('login/', LoginView.as_view(), name="login"),
	path('logout/', LogoutView.as_view(), name="logout"),
	path('reset-password/', PasswordResetView.as_view(), name="password-reset")
]
