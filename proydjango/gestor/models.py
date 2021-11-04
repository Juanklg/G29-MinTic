from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30,blank=False,default="nulo")
    direccion=models.CharField(max_length=50,blank=False,default="nulo")
    email=models.EmailField(max_length=50,unique=True,blank=False,default="nulo")    
    telefono=models.CharField(max_length=15,blank=False,default="nulo")
    password=models.CharField(max_length=15,blank=False,default="nulo")
    def __str__(self):
        return f"Nombre_del_Cliente: {self.nombre} - Email_del_cliente: {self.email}"

class Articulo(models.Model):
    nombre=models.CharField(max_length=30,unique=True)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self):
        return f'{self.nombre} de la seccion {self.seccion} $ {self.precio}'

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()