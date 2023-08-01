from django.views import generic
from rest_framework.views import Response
from .models import Product
from .serializers import ProductSerializer

class ProductList(generic.ListView):
    queryset = Product.objects.all()
    seriaizer_class = ProductSerializer
    