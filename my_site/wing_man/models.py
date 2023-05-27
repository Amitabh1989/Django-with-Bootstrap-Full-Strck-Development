from django.db import models



# Create your models here.
class WingManConfig(models.Model):
    raid = models.CharField(max_length=154, null=True, blank=False)
    drivees = models.PositiveIntegerField(default=0)
    init = models.CharField(max_length=154, null=True, blank=False)
    step_ref = models.CharField(max_length=154, null=True, blank=False)
    expected_res = models.CharField(max_length=154, null=True, blank=True)





