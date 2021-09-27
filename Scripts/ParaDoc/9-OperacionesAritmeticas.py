x = int(input("Digite un valor para x : "))
y = int(input("Digite un valor para y : "))

print("x es de tipo = ",type(x))
print("y es de tipo = ",type(y))
# --------------------------------------------------------
suma = x + y
print(f'Resultado suma: {suma} ')
resta = x - y
print(f'Resultado resta: {resta} ')
multiplicacion = x * y
print(f'Resultado multiplicación: {multiplicacion}')
#todas las divisiones con un solo slash(/) retornan el resultado en tipo(type) float(Coma flotante)
division = x / y
print(f'Resultado división: {division}')
print(type(division))
print(round(division,3))
division = x // y
print(f'Resultado división (int): {division}')
modulo = x % y
print(f'Resultado residuo división (módulo): {modulo}')
exponente = x ** y
print(f'Resultado exponente: {exponente}')
# --------------------------------------------------------

x = x + y
print(x)
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)