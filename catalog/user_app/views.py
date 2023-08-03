from rest_framework.views import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(["POST"])
def register_view(request):
    
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration successful!"
            data['username'] = account.username
            data['email'] = account.email
            
            return Response(data)
        else:    
            data = serializer.errors
            
        return Response(data)

@api_view(["POST",])
@permission_classes([IsAuthenticated]) 
def logout_view(request):
    
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)