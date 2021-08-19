#Bucle tipo for
arreglo = range(10,15)
print(type(arreglo))
print(len(arreglo))

for valor in arreglo:    
    print(valor)
else:
    print(f"Imprimio todos los valores")

miRange = range(1,11)
print(f"la logitud de miRange es {len(miRange)} valores")
print(miRange)

texto = "Hola Grupo 61 de python"

#for para recorrer objetos
for valor in miRange:
    print(valor)

for caracter in texto:
    print(caracter)

def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))
    for x in var:
        # if x==7:break
        print("El valor que toma x en el for es :",x)
    return 

# Los int no son iterables
var = 567986
detailVar(var)
#para iterar un int debemos convertirlo con str
var = 567986
detailVar(str(var))
#los str si son iterables
text = "Hola fundamentos de programacion Hola, Grupo 29 Hola"
detailVar(var)