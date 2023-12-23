from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path('', views.home, name="index"),
    path('busqueda/', views.busqueda, name="productos-buscar"),
    path('crear/', views.crear, name="crear"),
]
