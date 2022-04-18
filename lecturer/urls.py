from . import views
from django.urls import path

app_name = 'lecturer'
urlpatterns = [
    path('', views.home, name='home'),
    path('take_attendance', views.take_attendance, name='take_attendance')
]
