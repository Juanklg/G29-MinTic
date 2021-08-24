#Primer script que corre mi aplicacion

#Variables (int,float,str,bool)
#iterables o colecciones = {range,list,tuple,dict,set}

#funciones -> {Fun.propias, Fun.python, Fun,Clase}
#Sentencias de control = {if, for, while}

def detailArch(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))
    for x in range(len(el)):
        print(f"Pos : {x} - Elemento : {el[x]}")
    # for x in el:
    #     print(f"Elemento : {x}")

def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))

def isLogin(user)->bool:
    login = None
    if user=="Login":
        login = True
        print("Usuario esta logueado")
    else:
        login = False
        print("Usuario no esta logueado, Chao")
        exit()
    return 

user = "Login"
isLogin(user)
#------------------------------------------------------    
## solo se ejecuta esto si el usuario es = 'Login'
print("Inicia la App")

Estudiantes = ['Ana', 'Ashley', 'Dayana', 'Juan D', 'Kevin', 'Mateo', 'Paulina', 'Ricardo', 'Samuel', 'Santiago', 'Tomas', 'Yaser']

#con al tupla puedo captura los elementos con un desembalaje
fruits = ("apple", "banana",  "cherry", "strawberry", "raspberry")
print(fruits)

#concatenar con signo +
t = ("pera",)
nt = fruits+t
print("Concat whit (+)",nt)

#Patron DSU -> organiza las tuplas segu un parametro
TupleEst = tuple(Estudiantes)
print(TupleEst)
#Decorate
listaDecorate = list()
for est in TupleEst:
    listaDecorate.append((len(est),est))
#Sort
print(listaDecorate.sort())
#undecorate
listaSortLen = list()
for lgt,name in listaDecorate:
    print(name)
    listaSortLen.append(name)

print(listaSortLen)

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


# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'