from turtle import *

def avanzar(a:int):
    a+=10
    fd(10)
    return a

def giro(g:int,side:str="D"):
    g+=1
    if side == "D":
        rt(90)
    elif side == "I":
        lt(90)
    return g

def robotSquare():
    avance = 0
    giros = 0
    while giros < 4:
        avance = avanzar(avance)
        if avance == 100:
            avance=0
            giros = giro(giros)
    else:
        print("El robot ha terminado")
            
robotSquare()

done()
            