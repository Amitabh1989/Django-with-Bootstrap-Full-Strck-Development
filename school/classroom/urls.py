from django.urls import path
from . import views

app_name = "classroom"

urlpatterns = [
    path('', views.HomeView.as_view(), name='classroom'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('teacher_form/', views.TeacherView.as_view(), name='teacher'),
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>', views.TeacherDeleteView.as_view(), name='teacher_delete'),
]