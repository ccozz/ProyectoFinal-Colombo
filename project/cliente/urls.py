from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.home, name="index"),
    path('busqueda/', views.busqueda, name="clientes-buscar"),
    path('crear/', views.crear, name="crear"),
    ##### CBV - CLIENTE
    path('cliente_list/', views.ClienteList.as_view(), name="cliente_list"),
    path('cliente_detail/<pk>', views.ClienteDetail.as_view(), name="cliente_detail"),
    path('cliente_create/', views.ClienteCreate.as_view(), name="cliente_create"),
    path('cliente_update/<pk>', views.ClienteUpdate.as_view(), name="cliente_update"),
    path('cliente_delete/<pk>', views.ClienteDelete.as_view(), name="cliente_delete"),
]
