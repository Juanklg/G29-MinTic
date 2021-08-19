#Primer script que corre mi aplicacion

#Variables (int,float,str,bool,range,list,dict,tuple)
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

## asi es una lista
lista = []
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

print(dir(usuario))

print("get",usuario.get("nombre"))
print("items",usuario.items())
print("keys",usuario.keys())
print("pop",usuario.pop("skills"))
print("values",usuario.values())
print("update",usuario.update(grupo=29))
print(usuario)
copiausuario = usuario.copy()

# limpiar
print("clear",usuario.clear())
# eliminar el diccionario
del usuario
print(usuario)

sec = ('python','zope','plone')
ver = dict(sec)
detailVar(ver)
# detailVar(miDiccionarioConstructor)

