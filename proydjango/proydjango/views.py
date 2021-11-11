from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect,render
# template
from django.template import Template,Context,loader
# auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# gestor
from gestor.models import *
from gestor.forms import UserRegisterForm
# python 
import datetime
import pdb  # pdb.set_trace()

# django User model and auth class

def usuarioAdd(req):
    diccionario = {
        'fecha':datetime.datetime.now(),
        'model':'usuarios',
        # 'theme':'Quartz',
        # 'theme':'Sketchy',
    }   
    if req.method == 'POST':
        form=UserRegisterForm(req.POST)
        if form.is_valid():            
            username=form.cleaned_data['username']
            form.save()
            messages.success(req,f'El usuario {username} fue creado con exito ')
    else:
        messages.success(req,f'Probando los mensajes')
        form=UserRegisterForm()
        # diccionario['usuarios']= User.objects.all()
    diccionario['formulario']= form
    return render(req,'Usuario.html',diccionario)

def usuarioLogin(req):    
    diccionario = {
        'fecha':datetime.datetime.now(),
        # 'model':'usuarios',
        # 'theme':'Quartz',
        # 'theme':'Sketchy',
    }
    if req.method == 'POST':
        form=AuthenticationForm(req,req.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(req,user)
                messages.success(req,f'Hola {username} bienvenido')
                return redirect('home')
            else:
                messages.error(req, f'Usuario o contraseña incorrectas')
        else:
            messages.error(req, f'Usuario o contraseña incorrectas')
    else:
        form=AuthenticationForm()
        # diccionario['usuarios']= User.objects.all()
    diccionario['formulario']= form
    return render(req,'Login.html',diccionario)

def usuarioLogout(req):
    logout(req)
    return redirect('login')

# Learn django

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