from django.shortcuts import render
from django.http import HttpResponseRedirect
from gestor.models import *
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
            articulos = Articulo.objects.filter(seccion__icontains=req.GET['search']) | articulo.objects.filter(nombre__icontains=req.GET['search'])
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
        errorDict['enombre']='Debe tener 10 digitos'
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
    fechaActual = datetime.datetime.now()
    clientes = Cliente.objects.all()
    diccionario = {
        'fecha':fechaActual,
        'model':'clientes',
        # 'theme':'Quartz',
        # 'theme':'Sketchy',
        'clientes':clientes.values()
    }
    return render(request,'Cliente.html',diccionario)

def clientesAdd(req):    
    fnombre=req.POST['nombre']
    fdireccion=req.POST['direccion']
    femail=req.POST['email']
    ftelefono=req.POST['telefono']
    fpassword=req.POST['password']
    fpasswordRep=req.POST['passwordRep']
    print(fnombre)
    pdb.set_trace()
    status=valid(nombre,direccion,email,telefono,password),
    msj='Validando'

    # if len(nombre)>=30:
    #     msj=f'el nombre del producto tiene una logintud superior a 30, {len(nombre)}'
    # else:
    #     # art = articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
    #     msj=f'el articulo {nombre} se agrego de forma exitosa, {len(nombre)}'
    return HttpResponseRedirect(f'/clientes/?msj={msj}')

