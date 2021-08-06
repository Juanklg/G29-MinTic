from turtle import *

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

inicioWindow = [-330,280]


# import turtle

#-----------------------------------------
speed(300)

up()#levantar el lapiz
goto(inicioWindow)

done()#------------------------------------------