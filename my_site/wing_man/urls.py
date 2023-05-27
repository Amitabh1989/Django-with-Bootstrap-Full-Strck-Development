from . views import *
from django.urls import include, path


urlpatterns = [
    path('config/', WingConfigView.as_view())
]

