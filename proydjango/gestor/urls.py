from django.contrib import admin
from django.urls import path
from gestor.views import *

urlpatterns = [
    path('articulos', articulos),
    path('articoloAdd/', articulosAdd),

    path('clientes', clientes),
    path('clientesAdd/', clientesAdd),

    # path('delete/', articulosAdd),
    # path('edit/', articulosAdd),
]
