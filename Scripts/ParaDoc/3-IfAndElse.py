# #definimos unas variables con un valor inicial
x = 10
y = 11
# #Variables type bool
# miBool = x == y
# print(f"miBool es de tipo {type(miBool)}, y tiene un valor de : {miBool}")

# # capturamos el texto que nos piden en el enunciado
# varInputBool = input("Ingrese True/False para la segunda variable (True/False):")
# print(f"El usuario ingreso en texto :{varInputBool}")

# # convirtiendo una entrada de texto a tipo bool
# if varInputBool == "True":
#     varInputBool=True
# else:
#     varInputBool=False

# print(f"La variable 'varInputBool' convertida a booleano = {varInputBool}")

# #Para trabajar con booleanos se utilizan las operaciones Logicas
# # vamos a ver 3 tipos de operaciones logicas
# #1-and, 2-or, 3-not

# #3-not con el not invertimos el valor de una variable booleana
# print(f"la variable miBool = {miBool} la invierto asi, 'not miBool'")
# miBool = not miBool
# print(f"la variable miBool ahora = {miBool}")

# if miBool == True and varInputBool == True:
#     print(f"Las 2 variables son verdaderas")
# elif miBool == True or varInputBool == True:
#     print(f"Alguna de las 2 es verdadera")
# else:
#     print(f"Ninguna de las dos variables es verdadera")

def cualEsMayor():
    if x < y:
        print("x es menor q y")
    elif x > y:
        print("x es mayor q y")
    else:
        print("x es igual a y")

#para no utilizar anidados
def operacionLogica():
    if 0<x and x<10:
        print("x es un numero positivo de un solo digito")


if x == y:
    print("x es igual a y")    
else:
    print("Entro al else")
    cualEsMayor()

nota1=60
nota2=80
nota3=70
nota4=30
nota5=50

notas = (nota1,nota2,nota3,nota4,nota5)
print(type(notas))
min = max = notas[0]
print(min)
print(max)