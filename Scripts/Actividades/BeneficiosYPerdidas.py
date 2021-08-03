#Todo lo que se asigna desde un input() es de tipo o type str(String,texto,cadenas de texto)
ingresos = input("Digite sus ingresos : ")
gastos = input("Digite sus gastos : ")

#si usamos el print con los elementos separados por coma(,) pueden ser de types diferentes
print("la var ingresos es de tipo = ",type(ingresos))
print("la var gastos es de tipo = ",type(gastos))

#try q significa intentar, hace una prueba de un bloque de codigo, si falla ejecuta el except, si no falla continua normal
try:
    ingresos = int(ingresos)
    gastos = int(gastos)
#se utiliza cuando falla el try
except:
    print("Debe digitar los valores en numeros")
    print("Corra de nuevo su aplicacion")
    exit()

#si concatenamos con el signo mas (+) solo se úede con var de tipo string(str)
print("Los ingresos fueron : "+str(ingresos))
print("Los gastos fueron : "+str(gastos))

#es la sentencia de preguntas q nos permite ejecutar el fracmento de codigo rcorrespondiente a el ejercicio
if ingresos > gastos:
    resultado = "ganacias"
    valorResultado = ingresos - gastos
#elif es una segunda opcion de comparacion para ejecutar otro bloque de codigo
elif ingresos == gastos:
    resultado = "equilibrado"
    valorResultado = "0 ganacias y 0 perdidas"
#else es el bloque de codigo q se ejecuta si ninguna de las anteriores comparaciones se cumple
else:
    resultado = "perdidas"
    valorResultado = gastos - ingresos

print("El resultado es : "+resultado+" con un valor de "+str(valorResultado))