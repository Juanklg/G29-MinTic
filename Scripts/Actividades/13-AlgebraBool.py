# es una disyuncion que valida si es divisible por 2 o por 3
#solo es verdadero si aplica alguno de los 2
n=7
print(f"esta comparacion retorna : {n%2 == 0 or n%3 == 0}")

#trasnformacion de not
x=10
y=5
print(f"esta comparacion retorna : {not x>y}")
#comparando numeros con booleanos
print(f"esta comparacion retorna : {0 or False}")
print(f"esta comparacion retorna : {1 and True}")

#validador de izq ha derecha
def palindromo(numero:int)->bool:
    centena=numero//100
    print(centena)
    decena=(numero-centena*100)//10
    print(decena)
    unidad=numero-centena*100-decena*10
    print(unidad)
    # if centena == unidad:
    #     res = True
    # else:
    #     res=False
    #Usando el if simplificado    
    res = True if centena==unidad else False
    return res

def espar(num:int)->bool:    
    # if num%2 == 0
    #     res = True
    # else:
    #     res = False
    # usando el if simplificado
    res = True if num%2==0 else False
    return res

def clasificar_chocolate(codigo:int)->str:
    if palindromo(codigo):
        res = "SWEET" if espar(codigo) else "BITTER"
        #es lo mismo q decir
        # if espar(codigo):
        #     res = "SWEET"
        # else:
        #     res = "BITTER"
    else:
        res = "CINNAMON" if espar(codigo) else "LIGHT"
        #es lo mismo q decir
        # if espar(codigo):
        #     res = "CINNAMON"
        # else:
        #     res = "LIGHT"
    return res

print(clasificar_chocolate(123))
print(clasificar_chocolate(222))
print(clasificar_chocolate(111))
print(clasificar_chocolate(505))
print(clasificar_chocolate(576))