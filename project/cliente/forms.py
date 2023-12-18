from django import forms
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class ClienteBuscarFormulario(forms.Form):
    apellido = forms.CharField()