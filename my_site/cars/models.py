from django.db import models
# from django.core.validators 
# Create your models here.


class CarsModel(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()
    
    def __str__(self) -> str:
        return f'Car brand {self.brand} is from year {self.year}'