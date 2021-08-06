x = int(input("Digite un valor para x : "))
y = int(input("Digite un valor para y : "))

print("x es de tipo = ",type(x))
print("y es de tipo = ",type(y))

resultado = x == y
print(f'Resultado == : {resultado}')

resultado = x != y
print(f'Resultado != : {resultado}')

resultado = x > y
print(f'Resultado > : {resultado}')

resultado = x >= y
print(f'Resultado >= : {resultado}')

resultado = x < y
print(f'Resultado < : {resultado}')

resultado = x <= y
print(f'Resultado: <= {resultado}')