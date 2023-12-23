from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path('', views.home, name="index"),
    path('busqueda/', views.busqueda, name="productos-buscar"),
    path('ver_productos', views.ver_productos, name="ver_productos"),
    path('crear/', views.crear, name="crear"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('editar/<int:id>', views.editar, name="editar"),
]
