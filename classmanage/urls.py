from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'classmanage'
urlpatterns = [
    path('', views.index, name='home'),
    #  path('video_feed', views.video_feed, name='video_feed'),
    path('addclass/', views.addClass, name='addclass'),
    path('deleteclass/<str:pk>/', views.deleteClass, name='deleteclass'),
    path('editclass/<str:pk>/', views.editClass, name='editclass'),
    path('updateclass/<str:pk>/', views.updateClass, name='updateclass'),


]
