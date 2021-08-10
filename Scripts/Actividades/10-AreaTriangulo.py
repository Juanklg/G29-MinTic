def area(lado1:float,lado2:float)->float:
    area = (lado1*lado2)/2
    return area

lado1 = 10.2
lado2 = 30.0

res = area(lado1,lado2)
print("El resultado del area es "+str(res))