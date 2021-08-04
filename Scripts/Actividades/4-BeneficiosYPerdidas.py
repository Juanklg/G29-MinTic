#todo lo9 que as9ignamos de un input llega como string(str)
ingresos = input("Digite los ingresos : ")
gastos = input("Digite los gastos : ")
resultado = "Nada"

#intentar ejecutar una linea de codigo  y verificar que no arroje un error
try:
    ingresos=int(ingresos)
    gastos=int(gastos)
#esta excepción se ejecuta si el bloque de codigo dentro del try llegaa fallar
except:
    print("El valor ingresado debe ser de tipo numerico o de type int")
    print("vuelva a correr la aplicacion")
    exit()

print(f"Los ingresos son = {ingresos}")
print(f"Los gastos son = {gastos}")

# los if nos permiten hacer una comparacion o una pregunta interna que nos retorna un valor de falso o verdadero
# si la condicon es verdaera, ejecuta el bloque q hay dentro del if
if ingresos > gastos:
    resultado = "ganancia"
    valorResultado = ingresos-gastos
# si la condicon del if no es verdaera, valida la siguiente condicion, y si se cumple, ejecuta el bloque q hay dentro del elif de la condicion
elif ingresos == gastos:
    resultado = "equilibrio"
    valorResultado = gastos-ingresos
#si ninguna de las condiciones se cumple ejecuta lo que hay dentro del bloque de else
else:
    resultado = "perdida"
    valorResultado = gastos-ingresos

print(f"El resultado es una {resultado} de {valorResultado} pesos")