from django.http import HttpResponse
from django.template import Template,Context
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
    doc = open(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\templates\layout.html')
    tpl = Template(doc.read())
    doc.close()
    ctx = Context()
    document = tpl.render(ctx)
    return HttpResponse(document)

def tareas(req):
    taskList = ['Migrar templates desde Flask','reciclar Header y fotter en templates']
    doc = open(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\templates\tareas.html')
    tpl = Template(doc.read())
    doc.close()
    ctx = Context({'taskList':taskList})
    document = tpl.render(ctx)
    return HttpResponse(document)

def fecha(req):
    fecha = datetime.datetime.now()
    documento = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>.::Fecha::.</title>
        </head>
        <body>
            <h1>Usted hizo el req en la fecha %s</h1>
        </body>
        </html>
    '''% fecha
    return HttpResponse(documento)