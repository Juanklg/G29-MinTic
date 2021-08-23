#asi se crea un diccionario
miDiccionario = {}
miDiccionarioConstructor = dict()
miDiccionarioConstructor = dict(copia=123.23)
miDiccionario = {"total":55,"descuento":True,"num":"15"}

miDiccionario = {"total":55,"descuento":True,15:"15"}
miDiccionarioConstructor = dict(nombre=5+2,telefono=3514647,edad=33,ciudad="Bogota",num="15")

usuario = {
    "nombre":"Nombre del usuario",
    "edad":23,
    "curso":"Curso de python",
    "skills":{
        "Programacion":True,
        "BaseDeDatos":False
    },
    "numMedallas":10,
}

print(usuario['curso'])

# Asi actualizamos uno de los valores de las llaves de un diccionario
usuario['curso']="Fundamentos de programacion"
usuario['nombre']="Juan"
# print(usuario['curso'])

#ver todas las funciones de la variable
# print(dir(usuario))

print("get",usuario.get("nombre"))
print("items",usuario.items())
print("keys",usuario.keys())
print("pop",usuario.pop("skills"))
print("values",usuario.values())
print("update",usuario.update(grupo=29))
print(usuario)
copiausuario = usuario.copy()

#recorrer los diccionarios con un for
for key, valor in usuario.items():
    print(key, valor)
esle: print('-----------------------')

for key in usuario.keys():
    print(key)
esle: print('-----------------------')

for value in usuario.values():
    print(value)
esle: print('-----------------------')

# limpiar
print("clear",usuario.clear())
# eliminar el diccionario
del usuario
print(usuario)