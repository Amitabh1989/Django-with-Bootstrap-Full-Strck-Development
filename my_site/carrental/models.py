from django.db import models

# Create your models here.
class Feedback(models.Model):
    review = models.TextField(max_length=1000)
    stars = models.IntegerField()

    def __str__(self) -> str:
        return f'Its a {self.stars} star review !!'
