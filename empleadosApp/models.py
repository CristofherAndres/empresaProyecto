from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=15)
    correo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=12)