from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsProductOwnerOrReadOnly

class ProductList(generics.ListAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        requested_user = self.request.user
        
        return Product.objects.filter(owner=requested_user)
    
    
class ProductCreate(generics.CreateAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        requested_user = self.request.user 
        
        serializer.save(owner=requested_user)
        
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsProductOwnerOrReadOnly]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        
        requested_user = self.request.user
        
        return Product.objects.filter(owner=requested_user)