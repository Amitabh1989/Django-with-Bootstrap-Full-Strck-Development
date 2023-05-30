from django.contrib import admin
from catalog.models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)