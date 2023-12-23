from django.urls import path
from django.shortcuts import render
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

app_name = "core"

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    ##### LOGIN
    path("registro/", views.registro_view, name="registro"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
]