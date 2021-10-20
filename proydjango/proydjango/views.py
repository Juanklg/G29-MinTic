from django.http import HttpResponse
from django.template import Template,Context,loader
import datetime

def calculo(req,fechaNacimiento,fechaFutura):
    doc = open(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\templates\calculo.html')
    tpl = Template(doc.read())
    doc.close()
    añoActual = datetime.datetime.now().year
    edadActual = añoActual-fechaNacimiento
    edadFutura = fechaFutura-fechaNacimiento
    ctx = Context({
        'fechaNacimiento':fechaNacimiento,
        'edadActual':edadActual,
        'edadFutura':edadFutura,
        'fechaFutura':fechaFutura
    })
    document = tpl.render(ctx)
    return HttpResponse(document)

def saludar(req):
    diccionario = {"titulo":'Pagina de bienvenida',}
    doc = open(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\templates\layout\layout.html')
    tpl = Template(doc.read())
    doc.close()
    ctx = Context(diccionario)
    document = tpl.render(ctx)
    return HttpResponse(document)

def tareas(req):
    taskList = ['Migrar templates desde Flask','reciclar Header y fotter en templates']
    doc = open(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\templates\tareas.html')
    tpl = Template(doc.read())
    doc.close()
    ctx = Context({
        'titulo':'Lista de tareas',
        'nameList':'Tareas Django',
        'taskList':taskList
    })
    document = tpl.render(ctx)
    return HttpResponse(document)

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