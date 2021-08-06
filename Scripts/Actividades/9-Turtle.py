from turtle import *
import random

def CreateSol():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()

def crearFigura(lados:int,long:int):
    color('#5D11CD','#11CD2F')
    begin_fill()
    for x in range(0,lados):
        fd(long)
        lt(360/lados)
    end_fill()

def polygono(nLados,longitud):
    for i in range(0,nLados):
        fd(longitud)
        lt(360/nLados)
    if longitud > 1:
        lt(3)
        polygono(nLados, longitud-1)

def branch(bl,angle):
    angle=random.randint(18,28)
    sf=random.uniform(0.6,0.8)
    size=bl/10
    pensize(size)
    if bl > 5:
        fd(bl)
        lt(angle)
        branch(sf*bl, angle)
        rt(angle*2)
        branch(sf*bl, angle)
        lt(angle)
        bk(bl)
    else:
        color('green')
        stamp()
        color("brown")

#definicion de parametros
inicioWindow = [-330,280]
#-----------------------------------------
color("brown")
lt(90)
speed(600)
branch(50, 45)
done()#------------------------------------------