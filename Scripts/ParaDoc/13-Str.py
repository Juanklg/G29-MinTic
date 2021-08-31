def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))
    # for x in var:
    #     # if x==7:break
    #     print("El valor que toma x en el for es :",x)
    return 

def printIndex(iterable):
    for x in range(0,len(iterable)):        
        print("La pos: {0} tiene el valor: {1}".format(x , iterable[x]))

# orden alfabetico
def ordenAlfabetico(palabra,palabra2):
    if palabra < palabra2:
        print("Tu palabra, "+palabra+", viene antes de "+palabra2)
    elif palabra > palabra2:
        print("Su palabra, "+palabra+", viene despues de "+palabra2)
    else:
        print("Su palabra es "+palabra2)

text = "Hola fundamentos de programacion Hola, Grupo 29 Hola"
detailVar(var)
#En estas lineas separamos en espacios el texto general con .split()
splitText = text.split(' ')
# detailVar(splitText)
printIndex(splitText)

#puedo guardar en una nueva variable la informacion de un elemento de la lista
nuevaVar = text[len(text)-1]
print(nuevaVar)

#capturando sub strings desde posiciones especificas
nuevaVar = text[5:10]
print(nuevaVar)
nuevaVar = text[:10]
print(nuevaVar)
nuevaVar = text[5:]
print(nuevaVar)
nuevaVar = text[5:5]
print(nuevaVar)

#Comparacion de strings
nuevaVar = text[0:4]
if nuevaVar == "Hola":
    print(nuevaVar, "si es igual a Hola")
else: 
    print(nuevaVar)

#orden alfabetico
ordenAlfabetico(nuevaVar,"Arroz")

nv = splitText[1]
detailVar(splitText[1])

#funciones de los str
nv=nv.capitalize()
print(nv)
nv=nv.upper()
print(nv)
nv=nv.lower()
print(nv)
nv=nv.isalpha()
print(nv)
nv=text.find('a',26,30)
print(nv)

nv= "Juan         "

print(len(nv))
nv = len(nv.strip())

nv=text.startswith('pro')
print(nv)
nv=text.startswith('Hola')
print(nv)
nv=text.endswith("29")
print(nv)

#con la funcion dir puedo ver las funciones q puedo utilizar con esa variable
# print(dir(text))

hexadecimal = 15
#caracteres especiales
nv = "El valor de \tvar es = %x" %hexadecimal
nv = "El valor de \nvar es = %x" %hexadecimal

nv = "El valor de var es = %X" %hexadecimal
print(nv)
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
for mes in meses:
    print("* %10s * %-10s *" %(mes,mes))

print('Titulo'.center(50,'-'))

flotante = 1/3
varTextoformateada = "El resulatdo del flotantes es %f pero formateado es %.2f"%(flotante,flotante)
print(varTextoformateada)




#contador de busqueda
nv=text
nv=nv.count("Hola")

# replace
nv=text
nv = nv.replace("Hola","->",2)

# print(nv)
# print(text.find("Hola"))
# printIndex(text)
#formateador
nv="Mi v1 = {color}, mi v2={nombre}, mi v3={Grupo}".format(color="red",nombre="Juan",Grupo="29")
nv="Mi v1 = {2}, mi v2={0}, mi v3={1}".format("red","Juan","29")

nv=text
nv=text+"hola "*10

nv="hola"
nv+=" buenos"
nv+=" dias"

print(nv)
detailVar(nv)