from rest_framework.views import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer

@api_view(["POST"])
def register_view(request):
    
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
