Estudiantes = ['Ana', 'Ashley', 'Dayana', 'Juan D', 'Kevin', 'Mateo', 'Paulina', 'Ricardo', 'Samuel', 'Santiago', 'Tomas', 'Yaser']

#con al tupla puedo captura los elementos con un desembalaje
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
rojo,amarillo,*otras, morado = fruits
rojo,amarillo,*otras, morado = Estudiantes
print(fruits)
print(rojo)
print(amarillo)
print(otras)
print(morado)

#concatenar con signo +
t = ("pera",)
nt = fruits+t
print("Concat whit (+)",nt)

#Patron DSU -> organiza las tuplas segu un parametro
TupleEst = tuple(Estudiantes)
print("Imprimiendo tupla",TupleEst)
#Decorate
listaDecorate = list()
for est in TupleEst:
    listaDecorate.append((len(est),est))
#Sort
listaDecorate.sort(reverse=True)
print("Imprimiendo decorate sort",listaDecorate)
#undecorate
listaSortLen = list()
for lgt,name in listaDecorate:
    print(name)
    listaSortLen.append(name)

print("Imprimiendo lista ordenada",listaSortLen)

#desembalaje o umpack
a,*b,c = listaSortLen
# print(a)
# print(b)
# print(c)

#el desembalaje se hace mejor sobre una tupla
props = ("nombre","edad","grupo","proyecto","username")
(nombre, edad, grupo,proyecto,username) = props

print(nombre)
print(edad)

#intercambiar valores entre variables
nombre,edad=edad,nombre

print(nombre)
print(edad)

#uso de la asignacion multiple en una linea
email = "jkltsd@python.org"
user,domain = email.split('@')

print(user)
print(domain)



# crear un diccionario de la lista de estudiantes

dicEstudiantes = dict.fromkeys(listaSortLen)
print(dicEstudiantes)

lTuples = dicEstudiantes.items()

#lista de tu´plas con valores genericos
nuevaListaTuple = list()
for est,x2 in dicEstudiantes.items():
    nuevaListaTuple.append((est,29,15))

print(nuevaListaTuple)

# crear un diccionario con tuplas como llaves
dicFinal = dict()
for key,grupo,edad, in nuevaListaTuple:
    dicFinal[(key,grupo)] = 15

print(dicFinal)
detailArch(nuevaListaTuple)
# print(dir(dicEstudiantes))