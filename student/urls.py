from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.home, name='home'),
    path('register_course/', views.register_courses, name='register_course'),
    path('get_courses', views.get_courses, name='get_courses'),
    path('save_courses', views.save_courses, name='save_courses')
]
