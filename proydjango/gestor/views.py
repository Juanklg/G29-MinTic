from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
# gestor
from gestor.models import *
# python 
import datetime
import pdb  # pdb.set_trace()

def articulosAdd(req):
    nombre = req.POST['nombre']
    seccion = req.POST['seccion']
    precio = req.POST['precio']
    if len(nombre)>=30:
        msj=f'el nombre del producto tiene una logintud superior a 30, {len(nombre)}'
    else:
        # art = Articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
        msj=f'el articulo {nombre} se agrego de forma exitosa, {len(nombre)}'
    return HttpResponseRedirect(f'/gestor/articulos/?msj={msj}')
    
def articulos(req):
    msj = ''
    conjunto = set()
    print()
    if len(req.GET)>=1:
        if 'search' in req.GET.keys():
            articulos = Articulo.objects.filter(seccion__icontains=req.GET['search']) | Articulo.objects.filter(nombre__icontains=req.GET['search'])
        else:
            articulos = Articulo.objects.all()

        if 'msj' in req.GET.keys():
            msj = req.GET['msj']
        else:
            msj = ''
    else:
        articulos = Articulo.objects.all()
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

def valid(nombre,direccion,email,telefono,password,passwordRep):
    errorDict = {}

    # Nombre
    if len(nombre)>30 or len(nombre)<3:
        errorDict['enombre']='La longitud debe ser mayor a 3 y menor a 30 caracteres'

    # direccion
    
    # email
    if len(email)==0:
        errorDict['eemail']='Debe ingresar un correo'
    emailBase = Cliente.objects.filter(email=email)
    if not len(emailBase)==0:
        errorDict['eemail']='Correo electronico no esta disponible'
    
    # telefono
    if not(len(telefono)==10):
        errorDict['etelefono']='Debe tener 10 digitos'
    for i in telefono:
        if ord(i) < 48 or ord(i) > 58:
            errorDict['etelefono']='El telefono no puede contener letras ni caracateres'
            break
    
    # password
    if len(password)>20 or len(password)<8:
        errorDict['epassword']='La contraseña debe ser mayor a 8 y menor a 20 caracteres'
    # passwordRep
    if len(passwordRep)>20 or len(passwordRep)<8:
        errorDict['epasswordRep']='La contraseña debe ser mayor a 8 y menor a 20 caracteres'
    if not password==passwordRep:
        errorDict['epasswordRep']='Las contraseñas no coinciden'

    return errorDict

def clientes(request):
    clientes = Cliente.objects.all()
    diccionario = {
        'fecha':datetime.datetime.now(),
        'model':'clientes',
        # 'theme':'Quartz',
        # 'theme':'Sketchy',
        'clientes':clientes.values()
    }
    return render(request,'clientes/Cliente.html',diccionario)

def clientesAdd(req):    
    nombre=req.POST['nombre']
    direccion=req.POST['direccion']
    email=req.POST['email']
    telefono=req.POST['telefono']
    password=req.POST['password']
    passwordRep=req.POST['passwordRep']
    
    # ejecuta funcion de validacion y retora un diccionario con los errores
    status=valid(nombre,direccion,email,telefono,password,passwordRep)
    if len(status)>0:
        # Si hay errores envia mensaje y crea diccionarios de respuesta
        diccionario = {'status':status,
            'cliente':{'nombre':nombre,'direccion':direccion,'email':email,'telefono':telefono,'password':password}
        }
        messages.error(req, 'Error en formularios de registro')
        return render(req,'clientes/Cliente.html',diccionario)
    else:
        cliente = Cliente.objects.create(nombre=nombre,direccion=direccion,email=email,telefono=telefono,password=password)
        messages.success(req, f'Cliente {nombre} registrado con exito')
        return redirect('/gestor/clientes')


