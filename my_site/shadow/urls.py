from django.urls import path
from . import views

app_name = 'shadow'

urlpatterns = [
    path('<int:num_page>/', views.num_page_view ),
    path('', views.render_view, name="example"),
    path('patients/', views.list_patients, name="patients"),
    path('variable/', views.render_variable_view, name="variable"),
    path('<module>/', views.modules_view, name="modules"),
]