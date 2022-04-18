from django.urls import path
from . import views


app_name = 'hod'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('add_lecturer',views.add_lecturer, name='add_lecturer'),
    path('manage_lecturer', views.manage_lecturer, name='manage_lecturer'),
    path('add_school', views.add_school, name='add_school'),
    path('add_department', views.add_department, name='add_department'),
    path("manage_department/", views.manage_department, name="manage_department"),
    path('add_session', views.add_session, name='add_session'),
    path("manage_session/", views.manage_session, name="manage_session"),
    path('add_student', views.add_student, name='add_student'),
    path('manage_student', views.manage_student, name='manage_student'),
    path("edit_student/<str:pk>", views.edit_student, name="edit_student"),
    path('add_course', views.add_course, name='add_course'),
    path('manage_course', views.manage_course, name='manage_course'),
    path('set_current_session', views.set_current_session, name='set_current_session'),
    path('set_current_semester', views.set_current_semester, name='set_current_semester'),
]
