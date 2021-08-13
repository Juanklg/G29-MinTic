
#Asi se ejecuta un while con una variable de un contador 
#que cambia la condicion de entrada y sale cuando es mayor

#importamos libreria de tiempo de python
# import time
# from time import *
from time import sleep

#Definicion de un while basico
def WhileBasico(): #disminuyendo    
    n=5
    while n > 0 :
        sleep(0.5)#tiempo en segundos
        print(n)
        # n=n-1
        n-=1
    print("Despegue!")

#Asi se ejecuta un bucle infinito
def cicloInfinito():
    condicion = True
    contador = 0
    while condicion:
        contador += 1
        print(f"Ejecutando un ciclo while {contador}")
        if contador == 10:
            break
        sleep(.5) #tiempo en segundos
    else:
        print("Fin del ciclo while")

#Factorial
def factorial(n: int) -> int:
    resultado = 1
    numero_actual = 2
    # while not numero_actual > n:
    while numero_actual <= n:
        print(f"Resultado de {numero_actual-1}! = {resultado}")
        # resultado = resultado * numero_actual
        resultado *= numero_actual
        sleep(0.5) #tiempo en segundos
        numero_actual += 1
    return resultado

def alejandose():
    i = 1
    while i > 0:
        print(i)
        i = i+ 1
    print("Terminé")

def saltarLaMeta():
    i = 1
    while i != 10:
        sleep(1) #tiempo en segundos
        print(i)
        i = i+ 2
    print("Terminé") 

def noIncrementoInterno():
    i = 1
    while i > 0:
        sleep(1) #tiempo en segundos
        print(i)
    # i = i+ 1
    print("Terminé")

def controladoPorEventoWhile():
    promedio, total, contar = 0.0, 0, 0
    print("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
    while grado != -1:
        total = total + grado
        contar = contar + 1
        print("Introduzca la nota de un estudiante (-1 para salir): ")
        grado = int(input())
        if grado == "-1":
            break
    else:
        promedio = total / contar
        print("Promedio de notas del grado escolar es: " + str(promedio))

def fibonacci():
    a , b = 0 , 1
    while b < 100:
        print(b)        
        a , b = b , a+b
        # var=a
        # a=b
        # b=b+var

# WhileBasico()
# cicloInfinito()
# res = factorial(7)
# print(res)
# alejandose()
# saltarLaMeta()
# noIncrementoInterno()
# controladoPorEventoWhile()
# fibonacci()

print("Fin del programa")