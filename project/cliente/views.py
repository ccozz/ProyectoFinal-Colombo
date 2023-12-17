from django.shortcuts import render, redirect
from . import models

def home(request):
    # llamada a la base de datos
    # instancio y llamo objetos
    clientes = models.Cliente.objects.all()
    # creo un diccionario para pasar como parámetro en el render donde le explico que voy a llamar a los objetos que traigo con la llamada a la DB
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)

def busqueda(request):
    cliente_nombre = models.Cliente.objects.filter(nombre__contains="John")
    context = {
        "cliente_nombre": cliente_nombre
    }
    return render(request, "cliente/busqueda.html", context)

from . import forms

def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm
    return render(request, "cliente/crear.html", {"form": form})