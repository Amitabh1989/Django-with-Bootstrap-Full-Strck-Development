from django.db import models

STARS = [
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
]
# Create your models here.
class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    stars = models.CharField(choices=STARS, max_length=1)
    review = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return f'Its a {self.stars} star review !!'
