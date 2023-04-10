from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'recogmanage'
urlpatterns = [
     path('', views.recogmanage, name='home'),
    #  path('video_feed', views.video_feed, name='video_feed'),
     path('delete-recognition/<str:pk>/', views.deleteRecognition, name='deleterognition'),
     path('deletestranger/<str:pk>/', views.deleteStranger, name='deleterstranger'),
     path('stranger/', views.ShowStranger, name='stranger'),
     path('deleteallstranger/', views.DeleteAllStranger, name='deleteaddstranger'),

]
