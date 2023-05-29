from django.urls import path
from . import views

app_name = "classroom"

urlpatterns = [
    path('', views.HomeView.as_view(), name='classroom'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('contact/', views.ContactFormView.as_view(), name='contact')
]