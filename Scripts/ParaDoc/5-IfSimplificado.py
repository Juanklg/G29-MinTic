def validadorCondicion(any):
    print("Se ingreso a la funcion",any)
    condicion = "verdadera" if any else "falsa" 
    return "La condicion es "+condicion

print(validadorCondicion(""))
print(validadorCondicion("A"))
print(validadorCondicion(0))
print(validadorCondicion(15))
print(validadorCondicion(False))
print(validadorCondicion(True))

#Metodos medio simplificado -----------------------------------------
# condicion = ""
# print(condicion)
# print("condicion verdadera") if condicion else print("Condicion false")
# condicion = "Hola"
# print(condicion)
# print("condicion verdadera") if condicion else print("Condicion false")
# condicion = 0
# print(condicion)
# print("condicion verdadera") if condicion else print("Condicion false")
# condicion = 1
# print(condicion)
# print("condicion verdadera") if condicion else print("Condicion false")
# condicion=True
# print(condicion)
# print("condicion verdadera") if condicion else print("Condicion false")
# condicion=False
# print(condicion)
# print("condicion verdadera") if condicion else print("Condicion false")

#Metodo sin simplificar------------------------------------------------------
# condicion = ""
# print(condicion)
# if condicion: print("Se cumple la condicion")
# else: print("No se cumple la condicion")

# condicion = "HOla como estas"
# print(condicion)
# if condicion: print("Se cumple la condicion")
# else: print("No se cumple la condicion")

# condicion = 0
# print(condicion)
# if condicion: print("Se cumple la condicion")
# else: print("No se cumple la condicion")

# condicion = 1
# print(condicion)
# if condicion: print("Se cumple la condicion")
# else: print("No se cumple la condicion")

# condicion=False
# print(condicion)
# if condicion: print("Se cumple la condicion")
# else: print("No se cumple la condicion")

# condicion=True
# print(condicion)
# if condicion: print("Se cumple la condicion")
# else: print("No se cumple la condicion")