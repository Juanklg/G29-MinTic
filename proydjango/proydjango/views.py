from django.http import HttpResponse
import datetime

def calculo(req,fechaNacimiento,fechaFutura):
    añoActual = datetime.datetime.now().year
    edadActual = añoActual-fechaNacimiento
    edadFutura = fechaFutura-fechaNacimiento
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
            <h1>El individuo nacio en el %s, hoy tiene %s años</h1>
            <h2>En el año %s tendra %s años</h2>
        </body>
        </html>
    '''% (fechaNacimiento, edadActual, fechaFutura, edadFutura)
    return HttpResponse(documento)

def saludar(req):
    return HttpResponse('Enviar respuesta desde django en nueva vista')

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