from django.shortcuts import render
from django.http import HttpResponseRedirect
from gestor.models import *

import pdb  # pdb.set_trace()

def articulosAdd(req):
    nombre = req.POST['nombre']
    seccion = req.POST['seccion']
    precio = req.POST['precio']
    if len(nombre)>=30:
        msj=f'el nombre del producto tiene una logintud superior a 30, {len(nombre)}'
    else:
        # art = articulo.objects.create(nombre=nombre,seccion=seccion,precio=precio)
        msj=f'el articulo {nombre} se agrego de forma exitosa, {len(nombre)}'
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

def clientes(req):
    # msj = ''
    # conjunto = set()
    # print()
    # if len(req.GET)>=1:
    #     if 'search' in req.GET.keys():
    #         articulos = articulo.objects.filter(seccion__icontains=req.GET['search']) | articulo.objects.filter(nombre__icontains=req.GET['search'])
    #     else:
    #         articulos = articulo.objects.all()

    #     if 'msj' in req.GET.keys():
    #         msj = req.GET['msj']
    #     else:
    #         msj = ''
    # else:
    #     articulos = articulo.objects.all()
    #     # filtro de rango de precio
    # listArticulos = list(articulos.values())
    # for item in articulos.values():
    #     conjunto.add(item['seccion'])
    
    # diccionario = {
    #     'articulos':listArticulos,
    #     'secciones':conjunto,
    #     'alert':{'tipo':'danger','msj':msj}
    # }
    return render(req,'clientes/registro.html')

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

