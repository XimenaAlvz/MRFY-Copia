from django.db import models

# Create your models here.

class Recipe(models.Model):
    IDReceta = models.IntegerField(primary_key=True)  # Clave primaria que coincide con la base de datos
    Nombre = models.CharField(max_length=100, null=False)
    Calorias = models.CharField(max_length=50, null=True)
    CarbHidratos = models.CharField(max_length=50, null=True)
    Proteinas = models.CharField(max_length=50, null=True)
    Grasas = models.CharField(max_length=50, null=True)
    Instrucciones = models.TextField(null=True)
    Etiquetas = models.CharField(max_length=100, null=True)
    Comentarios = models.TextField(null=True)
    Valoración = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    TiempoPreparación = models.CharField(max_length=50, null=True)
    Ingredientes = models.TextField(null=True)

    def __str__(self):
        return self.name