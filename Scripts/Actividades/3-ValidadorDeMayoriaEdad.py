nombre = input("Ingrese su nombre : ")
edad = input("Ingrese su edad : ")

#el try nos ayuda a validar que se puede ejecutar una sentencia
#en caso q se cumpla el programa sigue y si no ejecuta lo que hay despues del except
#intentar ejecutar una linea de codigo  y verificar que no arroje un error
try:edad = int(edad)
#esta excepción se ejecuta si el bloque de codigo dentro del try llegaa fallar
except:
    print("El valor ingresado de edad debe ser de tipo numerico")
    print("vuelva a correr la aplicacion")
    exit()

#asi de concatena texto con variables utilizando el print y una f dentro de la definicion antes de las comillas
print(f"el nombre es de tipo {type(nombre)}")
print(f"la edad es de tipo {type(edad)}")

# asi funciona el if para preguntar si una condicion es valida
if type(edad)==int:
    #si la condicion es valida ejecuta lo qhay despues del if y del espacion de identacion
    if edad >= 18:
        print(f"{nombre} es mayor de edad, tiene {edad} años")
    #si la condicion no se cumple ejecuta la sentencias q estas despues del else y con su respectivo espacio
    else:
        print(f"{nombre} es menor de edad, tiene {edad} años")
else:
    print(f"{edad} no esta en formato numerico")
    exit()
#asi se hace comentarios de multiples lineas
"""
#Asi de hace un comentario de multiples lineas
print("su nombre es : "+nombre)
var = 10
print(var)
"""