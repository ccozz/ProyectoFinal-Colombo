from django import forms
from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"

class ProductoBuscarFormulario(forms.Form):
    nombre = forms.CharField()