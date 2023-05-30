"""
URL configuration for shadow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.shortcuts import render
# In case we want to redirect the user to catalog page by default, include
# the below line
# path('', RedirectView.as_view(url='catalog/'))

urlpatterns = [
    path("", lambda request: render(request, "index.html"), name="index"),
    # path('', RedirectView.as_view(url='catalog/')),
    path("admin/", admin.site.urls),
    path("testcase/", include("testcase.urls")),
    path("config/", include("config.urls"))
]
