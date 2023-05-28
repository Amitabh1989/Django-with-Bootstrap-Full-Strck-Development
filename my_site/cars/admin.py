from django.contrib import admin
from cars.models import CarsModel

# Register your models here.

# admin.site.register(CarsModel)
class CarsModelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TIME INFORMATION', {"fields": ["year"]}),
        ('BRAND INFORMATION', {"fields": ["brand"]}),
    ]

admin.site.register(CarsModel, CarsModelAdmin)