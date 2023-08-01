from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2, 
                                validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(unique=False, upload_to="media/Products-Avatar/", blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
