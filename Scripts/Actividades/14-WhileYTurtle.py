from turtle import *

pd()

def movimientos():
    # promedio, total, contar = 0.0, 0, 0
    print("Introduzca letra para el movimiento (ex para salir)")
    letra = input()
    while letra != "ex":
        if letra=="a": fd(50)
        elif letra=="b": bk(50)
        elif letra=="d": rt(45)
        elif letra=="i": lt(45)
        elif letra=="u": up()
        elif letra=="w": pd()
        else: print("Esta letra no tiene un movimiento asignado")
        print("Introduzca letra para el movimiento (ex para salir)")
        letra = input()
    else:
        print("Figura terminada")
        pu()
        home()
        done()

movimientos()