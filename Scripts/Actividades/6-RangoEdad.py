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

#solo apto para personas menores de 15, entre 20 y 25 y mayores de 30
#es decir los que tiene entre 15 y 20 y entre 25 y 30 no aplican

print(id(edad))

if edad<15 or (edad >=20 and edad<=25) or edad>30:
    print("es apto para ingresar")
else:
    print("no es apto para ingresar")

