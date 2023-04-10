from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'facultymanage'
urlpatterns = [
    path('', views.index, name='home'),
    #  path('video_feed', views.video_feed, name='video_feed'),
    path('addfaculty/', views.addfaculty, name='addfaculty'),
    path('deletefaculty/<str:pk>/', views.deletefaculty, name='deletefaculty'),
    path('editfaculty/<str:pk>/', views.editfaculty, name='editfaculty'),
    path('updatefaculty/<str:pk>/', views.updatefaculty, name='updatefaculty'),



]
