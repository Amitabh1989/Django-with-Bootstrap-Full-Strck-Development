from django.urls import path
from . import views

app_name = "carrental"

urlpatterns = [
    path("review/", views.feedback_view, name="review"),
    path("thanks/", views.thankyou_view, name="thanks")
]
