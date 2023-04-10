from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'studentmanage'
urlpatterns = [
     path('', views.index, name='home'),
    #  path('video_feed', views.video_feed, name='video_feed'),
     path('addstd/', views.addStudent, name='addstd'),
     path('delete-std/<str:pk>/', views.deleteStudent, name='deletestd'),
     path('edit-std/<str:pk>/', views.editStudent, name='editstd'),
     path('update-std/<str:pk>/', views.updateStudent, name='updatestd'),
     
]
