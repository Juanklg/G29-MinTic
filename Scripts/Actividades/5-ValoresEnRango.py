valor = int(input('Escribe el valor(Solo numeros): '))
valorMinimo = 0
valorMaximo = 5

dentroRango = valor >= valorMinimo and valor <= valorMaximo
print(f"dentroRango = {dentroRango}")

if dentroRango:
    print(f'El valor {valor} está dentro de rango')
else:
    print(f'El valor {valor} está fuera de rango')