from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import json

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(40), MaxValueValidator(160)])

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} is {self.age} years old'
    