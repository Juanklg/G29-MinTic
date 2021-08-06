
#Asi se ejecuta un while con una variable de un contador 
#que cambia la condicion de entrada y sale cuando es mayor
import time
contador = 0
numeroIteraciones = 10

def printContador(cont2):    #pass
    print(f"Iteracion n° {cont2}")

def retardoYaumento(cont,incre=2):
    printContador(cont)
    time.sleep(1)#tiempo en segundos
    cont += incre
    return cont

while contador <= numeroIteraciones:
    incremento = 1
    contador = retardoYaumento(contador,incremento)
else:
    print("Fin del ciclo while")

#Asi se ejecuta un bucle infinito
# condicion = True
# while condicion:
#     print("Ejecutando un ciclo while")
#     time.sleep(5)#tiempo en segundos
# else:
#     print("Fin del ciclo while")