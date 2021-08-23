#Primer script que corre mi aplicacion

#Variables (int,float,str,bool)
#iterables o colecciones = {range,list,tuple,dict,set}

#funciones -> Fun.propias, Fun.python
#bucles (while,for)

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

def detailArch(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))
    for x in range(len(el)):
        print(f"Pos : {x} - Elemento : {el[x]}")
    # for x in el:
    #     print(f"Elemento : {x}")

def buscarYeliminar(lista,parametro):
    pos = lista.index(parametro)
    lista.pop(pos)
    return lista

#comparacion de estructuras de datos
lista = ['Juan','Karla','Ricardo', 'María']
tupla = ('Naranja', 'Plátano', 'Guayaba')
conjunto = {'Marte', 'Júpiter', 'Venus'}

#imprimir elementos
# detailArch(lista)
# detailArch(tupla)
# detailArch(conjunto)

#el conjunto no permite indexacion
# print(lista[1])
# print(lista[-1])
# print(tupla[1])
# print(tupla[-1])

#validar si existe dentro de la estructura
# print('Karla' in lista)
# print('Plátano' in tupla)
# print('Marte' in conjunto)

#verificar metodos comunes
detailArch(lista)
lista.append('Ashley')  # append
lista.insert(1,'Juan')  # insert
print('Cuantas veces esta juan =',lista.count('Juan')) # count

grupo29 = (
    'Ana',
    'Dayana',
    'Juan D',
    'Kevin',
    'Mateo',
    'Paulina',
    'Samuel',
    'Santiago',
    'Tomas'
)
detailArch(grupo29)
print('Buscando index en pos :',grupo29.index('Paulina'))
print('Count con la tupla : ',grupo29.count('Kevin')) # count

#convertimos a tupla del grupo 29 en una lista
ListGrupo29 = list(grupo29)

detailArch(ListGrupo29)
#lista orignal de estudiantes
detailArch(lista)
#la lista original le agrega la informacion de la lista del grupo 29
lista.extend(ListGrupo29)#extend
detailArch(lista)
# Antes de organizar la lista la invertimos manteniendo su posicion de ingreso
lista.reverse()
detailArch(lista)
#la lista la vamos a organizar
lista.sort(reverse=True)
detailArch(lista)
lista.sort()
detailArch(lista)

# ahora usamos el'remove' que elimina el primer elemento q encuentra con ese nombre
lista.remove('Juan')
detailArch(lista)
#Buscamos a Juan para sacarlo de la lista
posJuan = lista.index('Juan')
print('Donde esta Juan',posJuan)
#aplicar el pop y elminar el ultimo de la lista si sepa alimpio o el indice se se pasa
lista.pop(posJuan)
detailArch(lista)
#usamos una funcion para buscar y elominar
lista=buscarYeliminar(lista,'Karla')
lista=buscarYeliminar(lista,'María')
detailArch(lista)
# clear
lista.clear()
detailArch(lista)

#con al tupla puedo captura los elementos con un desembalaje
fruits = ("apple", "banana",  "cherry", "strawberry", "raspberry")
print(fruits)

(princ, *secun, penultimo,ultimo) = fruits

print(princ)
print(secun)
print(penultimo)
print(ultimo)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'



