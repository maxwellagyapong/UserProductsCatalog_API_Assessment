from django.urls import path
from .views import ProductList, ProductCreate, ProductDetail

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('create/', ProductCreate.as_view(), name='create-product'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
