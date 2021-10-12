from django.http import HttpResponse

def saludar(req):
    
    return HttpResponse('Enviar respuesta desde django en nueva vista')