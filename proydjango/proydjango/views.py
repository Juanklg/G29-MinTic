from django.http import HttpResponse
from django.template import Template,Context,loader
import datetime

from django.shortcuts import render
def articulos(req):
    return render(req,'articulos.html')

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