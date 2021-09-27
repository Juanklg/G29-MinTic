#List

def detailArch(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))
    # for x in range(len(el)):
    #     print("Pos : "+x+" - Elemento : "+el[x])
    for x in el:
        print(f"Elemento : {x}")

def buscarYeliminar(lista,parametro):
    pos = lista.index(parametro)
    lista.pop(pos)
    return lista

#comparacion de estructuras de datos
lista = ['Juan','Karla','Ricardo','María']
tupla = ('Naranja', 'Plátano', 'Guayaba')
conjunto = {'Marte', 'Júpiter', 'Venus'}

#imprimir elementos
detailArch(lista)
detailArch(tupla)
# detailArch(conjunto)

#el conjunto no permite indexacion
print(lista[1])
print(lista[-1])
print(tupla[1])
print(tupla[-1])

#validar si existe dentro de la estructura
print('Karla' in lista)
print('Plátano' in tupla)
print('Marte' in conjunto)

#verificar metodos comunes
detailArch(lista)
lista.append('Ashley')  # append
lista.insert(1,'juan')  # insert
print('Cuantas veces esta juan =',lista.count('Juan')) # count

grupo29 = ( # Tupla de estudiantes
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

#convertimos la tupla del grupo 29 en una lista
ListGrupo29 = list(grupo29)

detailArch(ListGrupo29)
#lista orignal de estudiantes
detailArch(lista)
#la lista original le agrega la informacion de la lista del grupo 29
lista.extend(ListGrupo29)#extend no solo funciona con listas sino tambien con tuplas
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
posJuan = lista.index('juan')
print('Donde esta Juan',posJuan)
#aplicar el pop y elminar el ultimo de la lista si sepa alimpio o el indice se se pasa
lista.pop(posJuan)
detailArch(lista)
#creamis una func de las ultimas lineas para buscar y eliminar a un integrante 
lista=buscarYeliminar(lista,'Karla')
lista=buscarYeliminar(lista,'María')
detailArch(lista)

print(dir(lista))
# clear
lista.clear()
detailArch(lista)

del lista
print(lista)