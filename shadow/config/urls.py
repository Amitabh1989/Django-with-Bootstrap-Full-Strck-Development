from django.urls import path
from config.views import *

app_name = "config"

urlpatterns = [
    path("", ConfigView.as_view(), name="config"),
    path("step_list/", StepList.as_view(), name="step_list"),
    path("step_details/<int:pk>", StepDetails.as_view(), name="step_details"),
    path('download/', StepsDownloadView.as_view(), name="steps_download"),
]