from django.db import models

class categorias(models.Model):
    tipo_categorias = [
        ('cat1', 'Servicios'),
        ('cat2', 'Escapes'),
        ('cat3', 'Motor'),
        ('cat4', 'Chasis'),
        ('cat5', 'Baterías'),
    ]

class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    categoria = models.CharField(max_length=50, choices=categorias.tipo_categorias)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'Producto: {self.nombre}\nPrecio:{self.precio}'