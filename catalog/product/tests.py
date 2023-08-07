from user_app.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@gmail.com", first_name="test",
                                        last_name="case", password="Password@123",)
    
        data = {
            "email": "test@gmail.com",
            "password": "Password@123"
        }
        
        login_respone = self.client.post(reverse("login"), data)
        
        self.response_body = login_respone.json()
        self.token = self.response_body['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token)
        
        self.product = Product.objects.create(owner=self.user,
                                              name="Apple Air", 
                                              price= 1599.99,
                                              quantity= 35,
            image ="http://127.0.0.1:8000/media/Products-Avatar/Screenshot_19_isoGqPd.png")                   

    def test_product_create_unauthorized(self):
        
        data = {
            "name": "Apple Air",
            "price": "1599.99",
            "quantity": 35,
            "image": "http://127.0.0.1:8000/media/Products-Avatar/Screenshot_19_isoGqPd.png"
        }
        
        response = self.client.post(reverse("create-product"), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_product_create_authorized(self):
        pass
        
    def test_product_list_unauthorized(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_product_list_authorized(self):
        pass
        
    def test_product_detail_unauthorized(self):
        response = self.client.get(reverse("products"), args=[self.product.pk])
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_product_detail_authorized(self):
        pass
        