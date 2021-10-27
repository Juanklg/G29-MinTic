from django.http import HttpResponse
from django.template import Template,Context,loader
import datetime

from django.shortcuts import render
from gestor.models import *

def articulosAdd(req):    
    nombre = req.GET['nombre']
    seccion = req.GET['seccion']
    precio = req.GET['precio']
    diccionario={
        'nombre' : nombre,
        'seccion':seccion,
        'precio':precio,
    }
    print(diccionario)
    art = articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
    print(art)
    return render(req,'articulos.html')

def articulos(req):
    articulos = articulo.objects.filter()
    listArticulos = list(articulos.values())
    # art = articulo.objects.filter(seccion='tecnologia')
    # art = articulo.objects.filter(precio__gt=90)
    diccionario = {
        'articulos':listArticulos
    }
    return render(req,'articulos.html',diccionario)

def calculo(req,fechaNacimiento,fechaFutura):    
    añoActual = datetime.datetime.now().year
    edadActual = añoActual-fechaNacimiento
    edadFutura = fechaFutura-fechaNacimiento
    diccionario={
        'fechaNacimiento':fechaNacimiento,
        'edadActual':edadActual,
        'edadFutura':edadFutura,
        'fechaFutura':fechaFutura
    }
    doc_externor=loader.get_template('calculo.html')
    documento=doc_externor.render(diccionario)
    return HttpResponse(documento)

def saludar(req):
    diccionario = {"titulo":'Pagina de bienvenida',}
    doc_externor=loader.get_template('layout/layout.html')
    documento=doc_externor.render(diccionario)
    return HttpResponse(documento)

def tareas(req):
    taskList = ['Migrar templates desde Flask','reciclar Header y fotter en templates']
    diccionario={
        'titulo':'Lista de tareas',
        'nameList':'Tareas Django',
        'taskList':taskList
    }
    doc_externor=loader.get_template('tareas.html')
    documento=doc_externor.render(diccionario)
    return HttpResponse(documento)

def fecha(req):
    fecha = datetime.datetime.now()
    diccionario = {
        'titulo':'Pagina de fecha',
        'fecha':fecha
    }
    doc_externor=loader.get_template('intro.html')
    documento=doc_externor.render(diccionario)
    return HttpResponse(documento)

def videos(req):
    fecha = datetime.datetime.now()
    diccionario = {
        'titulo':'Pagina de videos',
        'fecha':fecha
    }
    doc_externor=loader.get_template('videos.html')
    documento=doc_externor.render(diccionario)    
    return HttpResponse(documento)