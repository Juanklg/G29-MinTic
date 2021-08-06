#esto es una constante con un  numero(int)
numero = 61
#los input(los input's siempre seran de type 'str',texto,string)
#capturamos el texto y lo almacenamos en x
x = input("Ingrese x (debe ser en numeros) :")
#capturamos el texto y lo almacenamos en y
y = input("Ingrese y (debe ser en numeros) :")

#definicion de multiples variables
var1 = var2 = var3 = 100
print(f"las var de la 1 a la 3 son = {var1},{var2},{var3}")
var1, var2, var3 = 100,200,300
print(f"las var de la 1 a la 3 son = {var1},{var2},{var3}")

try:
    x=int(x)
    y=int(y)
except:
    print("El valor ingresado debe ser de tipo numerico o de type int")
    print("vuelva a correr la aplicacion")
    exit()

print(f"x es de tipo {type(x)}")
print(f"y es de tipo {type(y)}")

suma = x+y
print(f"el resultado de suma es: {suma}")

resta = x-y
print(f"el resultado de resta es {resta}")

multiplicacion = x*y
print(f"el resultado de multiplicacion es {multiplicacion}")

#el resultado de las divisiones siempre es un flotante(float)
division = x/y
print(f"el resultado de division es {division}")
print(type(division))

division2 = x//y
print(f"el resultado de division entera es {division2}")

modulo = x%y
print(f"el resultado de modulo es {modulo}")

expo = x**y
print(f"el resultado de expo es {expo}")