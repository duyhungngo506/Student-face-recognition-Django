from django.contrib import admin
from django.urls import path, include
from . import views
app_name= 'login'
urlpatterns = [
     path('', views.getLogin, name='login'),
     path('/postLogin', views.postLogin, name='postlogin'),
     path('/logout', views.Logout, name='logout'),


]
