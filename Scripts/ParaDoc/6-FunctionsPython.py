
v1,v2,v3,v4,v5 = 85,63,12,69,74

print(v1,v2,v3,v4,v5,sep=' - ',end=' Son los valores ingresados\n')

maximo = max(v1,v2,v3,v4,v5)
print(f"Valor maximo = {maximo}")
minimo = min(v1,v2,v3,v4,v5)
print(f"Valor minimo = {minimo}")
suma = sum((v1,v2,v3,v4,v5))
print(f"Valor de la suma = {suma}")
texto = "Hola Grupo 61 de python"
print(f"la logitud de texto es {len(texto)} caracteres")
print(texto[0],texto[5])

miRange = range(5,10)
print(f"la logitud de miRange es {len(miRange)} valores")
print(miRange)

for valor in range(2,10):
    print(valor)

# help(print)

