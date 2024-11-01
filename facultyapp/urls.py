from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'facultyapp'

urlpatterns = [
    path('', views.FacultyHomePage, name='FacultyHomePage'),

    # path('blog_list/', views.blog_home, name='blog_list'),
    # path('blog/<slug:slug>/', views.blog_home, name='blog_detail'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<int:pk>/delete/', views.delete_task, name='delete'),
    path('add_course/',views.add_course,name='add_course'),
    path('view_student_list/',views.view_student_list,name='view_student_list'),

]