from django.shortcuts import render
from . import models

def home(request):
    # llamada a la base de datos
    # instancio y llamo objetos
    clientes = models.Cliente.objects.all()
    # creo un diccionario para pasar como parámetro en el render donde le explico que voy a llamar a los objetos que traigo con la llamada a la DB
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)
