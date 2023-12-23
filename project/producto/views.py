from django.shortcuts import render, redirect
from . import models
from .forms import ProductoBuscarFormulario
from . import forms

def home(request):
    """ return render(request, "producto/index.html") """
    productos = models.Producto.objects.all()
    context = {"productos": productos}
    return render(request, "producto/index.html", context)

def busqueda(request):
    if request.method == "GET":
        form = ProductoBuscarFormulario()
        return render(request, "producto/busqueda.html", context={"form": form})
    else:
        formulario = ProductoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            # Accede al campo correcto del formulario
            nombre = informacion["nombre"]

            # Utiliza el método icontains para la búsqueda de subcadena sin importar mayúsculas y minúsculas
            productos_filtrados = models.Producto.objects.filter(nombre__icontains=nombre)

            contexto = {"productos": productos_filtrados}
            return render(request, "producto/productos_list.html", contexto)
        else:
            # Manejar el caso cuando el formulario no es válido
            return render(request, "producto/busqueda.html", context={"form": formulario})

def ver_productos(request):
    productos = models.Producto.objects.all()
    context = {"productos": productos}
    return render(request, "producto/productos_list.html", context)

def crear(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.ProductoForm()
    return render(request, "producto/crear.html", {"form": form})


def eliminar(request, id):
    if request.method == "POST":
        producto = models.Producto.objects.get(id=id)
        producto.delete();

        productos = models.Producto.objects.all()
        return render(request, "producto/productos_list.html", {"productos": productos})

def editar(request, id):
    producto = models.Producto.objects.get(id=id)

    if request.method == "POST":
        form = forms.ProductoForm(request.POST, instance=producto)
        
        if form.is_valid():
            form.save()
            return redirect("producto:index")
        else:
            return render(request, "producto/editar.html", {"form": form, "id": producto.id})
        
    else:
        form = forms.ProductoForm(instance=producto)
        return render(request, "producto/editar.html", {"form": form, "id": producto.id})