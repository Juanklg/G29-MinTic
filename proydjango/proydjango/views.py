from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context,loader
import datetime

from django.shortcuts import render
from gestor.models import *

def articulosAdd(req):    
    nombre = req.GET['nombre']
    seccion = req.GET['seccion']
    precio = req.GET['precio']
    art = articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
    msj=f'{nombre} agregado correctamente'
    return HttpResponseRedirect(f'/articulos/?msj={msj}')

    
def articulos(req):
    msj = ''
    conjunto = set()
    print()
    if len(req.GET)>=1:
        if 'search' in req.GET.keys():
            articulos = articulo.objects.filter(seccion__icontains=req.GET['search']) | articulo.objects.filter(nombre__icontains=req.GET['search'])
        else:
            articulos = articulo.objects.all()

        if 'msj' in req.GET.keys():
            msj = req.GET['msj']
        else:
            msj = ''
    else:
        articulos = articulo.objects.all()
        # filtro de rango de precio
    listArticulos = list(articulos.values())
    for item in articulos.values():
        conjunto.add(item['seccion'])
    
    diccionario = {
        'articulos':listArticulos,
        'secciones':conjunto,
        'alert':{'tipo':'danger','msj':msj}
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
        'fechaFutura':fechaFutura,

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


    # art = articulo.objects.filter(seccion='tecnologia')
    # art = articulo.objects.filter(precio__gt=90)    