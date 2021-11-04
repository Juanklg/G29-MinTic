from django.contrib import admin
from django.urls import path
from gestor.views import *

urlpatterns = [
    path('articulos/', articulos),
    path('articuloAdd/', articulosAdd),

    path('clientes/', clientes),
    path('clienteAdd/', clientesAdd),

    # path('delete/', articulosAdd),
    # path('edit/', articulosAdd),
]
