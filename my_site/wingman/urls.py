from django.urls import path
from . import views

urlpatterns = [
    path('<int:num_page>/', views.num_page_view ),
    path('<module>/', views.modules_view, name="modules"),
    path('', views.render_view, name="example"),
]