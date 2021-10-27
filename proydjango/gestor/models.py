from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)    
    telefono=models.CharField(max_length=15)

class articulo(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self):
        return f'{self.nombre} de la seccion {self.seccion} $ {self.precio}'



class pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()