from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add.html', views.add, name="add"),
    path('subtract.html', views.subtract, name="subtract"),
    path('multiplication.html', views.multiplication, name="multiply"),
    path('division.html', views.division, name="divide"),
    path('login.html', views.loginUser, name="login"),
    path('logout.html', views.logoutUser, name="logout"),
    path('register.html', views.registerUser, name="register"),
    path('editProfile.html', views.editProfile, name="editUser"),
    path('changePassword.html', views.changePassword, name="changePassword"),
    path('resume.html', views.resume, name="resume"),
    path('countdown.html', views.countdown, name="countdown"),
]
