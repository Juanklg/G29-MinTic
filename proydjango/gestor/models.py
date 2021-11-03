from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre=models.CharField(max_length=30,blank=False,default="nulo")
    direccion=models.CharField(max_length=50,blank=False,default="nulo")
    email=models.EmailField(max_length=50,unique=True,blank=False,default="nulo")    
    telefono=models.CharField(max_length=15,blank=False,default="nulo")
    password=models.CharField(max_length=15,blank=False,default="nulo")

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