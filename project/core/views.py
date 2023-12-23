from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserCreationFormulario, UserEditionFormulario

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def login_view(request):

    if request.user.is_authenticated:
        return render(request, "core/index.html", {"mensaje": f"Ya estás autenticado: {request.user.username}"})

    if request.method == "GET":
        return render(request, "core/login.html", {"form": AuthenticationForm()})
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(request, "core/index.html", {"mensaje": f"Bienvenido {modelo.username}"})
        else:
            return render(request, "core/login.html", {"form": formulario})

def logout_view(request):
    pass


def registro_view(request):

    if request.method == "GET":
        return render(request, "core/registro.html", {"form": UserCreationFormulario()})
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(request, "core/index.html", {"mensaje": f"Usuario creado: {usuario}"})

        else:
            return render(request, "core/registro.html", {"form": formulario})