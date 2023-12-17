from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.home, name="index"),
    path('busqueda/', views.busqueda),
    path('crear/', views.crear),
]
