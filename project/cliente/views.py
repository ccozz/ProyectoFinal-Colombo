from django.shortcuts import render, redirect
from . import models
from .forms import ClienteBuscarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    # llamada a la base de datos
    # instancio y llamo objetos
    clientes = models.Cliente.objects.all()
    # creo un diccionario para pasar como parámetro en el render donde le explico que voy a llamar a los objetos que traigo con la llamada a la DB
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)

def busqueda(request):
    if request.method == "GET":
        form = ClienteBuscarFormulario()
        return render(request, "cliente/busqueda.html", context={"form": form})
    else:
        formulario = ClienteBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            # Accede al campo correcto del formulario
            apellido = informacion["apellido"]

            # Utiliza el método icontains para la búsqueda de subcadena sin importar mayúsculas y minúsculas
            clientes_filtrados = models.Cliente.objects.filter(apellido__icontains=apellido)

            contexto = {"clientes": clientes_filtrados}
            return render(request, "cliente/clientes_list.html", contexto)
        else:
            # Manejar el caso cuando el formulario no es válido
            return render(request, "cliente/busqueda.html", context={"form": formulario})


from . import forms

def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})

# Vistas basadas en clases
class ClienteList(LoginRequiredMixin, ListView):
    # con esto sabe que registros buscar
    model = models.Cliente
    # los renderiza en el siguiente template
    template_name = 'clientes/cliente_list.html'
    # los encuentro bajo la siguiente key
    context_object_name = "clientes"

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = models.Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = "cliente"

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = models.Cliente
    template_name = 'clientes/cliente_create.html'
    fields = ["nombre", "apellido", "nacimiento", "email", "provincia"]
    success_url = "cliente:clientes_list"

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = models.Cliente
    template_name = 'clientes/cliente_update.html'
    fields = ["nombre", "apellido", "nacimiento", "email", "provincia"]
    success_url = "cliente:clientes_list"

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = models.Cliente
    template_name = 'clientes/cliente_delete.html'
    success_url = "cliente:clientes_list"