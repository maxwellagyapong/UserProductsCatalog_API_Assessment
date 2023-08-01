from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2, 
                                validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(unique=True, upload_to="media/Products-Avatar/", blank=True)
    
    def __str__(self) -> str:
        return self.name
