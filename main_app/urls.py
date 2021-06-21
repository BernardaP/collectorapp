from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('students/', views.students_index, name='index'),
    path('students/<int:student_id>/', views.student_detail, name='detail'),
    path('students/<int:student_id>/add_canvas/', views.add_canvas, name='add_canvas')
]
