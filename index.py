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

def detailArchZip(el):
    print('---------------------------------')
    print(el)
    print("len = ",len(el))

    for i,valor in zip(range(len(el)),el):
        # print(i,valor)
        print(f"{i} - Elemento : {valor}")
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
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

#creacion de conjuntos por emdio de listas, tuplas y range
s = set(range(1,7))
s1 = set(Estudiantes)
s2 = set(fruits)

texto = "Hola grupo 29 desde python set's"
print(len(texto))
s3 = set(texto)

detailArchZip(s)
detailArchZip(s1)
# detailArchZip(s2)
# detailArchZip(s3)

# dir(s)
# operaciones de conjuntos
#union
s4 = s2 | s1
detailArchZip(s4)
#intersection
s5 = s4 & s2
print("s5")

detailArchZip(s4)
detailArchZip(s5)

#funciones

# 'add',
print("add",s5.add('Mateo'))
# 'clear'
print("clear",s3.clear())
detailArchZip(s3)
# 'copy'
print("copy")
s3=s4.copy()
# 'difference'
print("difference 3 y 4",s3.difference(s4))
print("difference 4 y 5",s4.difference(s5))
print("difference 5 y 3",s5.difference(s3))
# 'difference_update'
print("difference_update 4 y 5",s4.difference_update(s5))
# 'discard'
print("discard",s4.discard('Samuel'))
# 'remove'
print("remove",s4.remove('Ana'))
# 'intersection'
print("intersection 3 y 4",s3.intersection(s4))
print("intersection 3 y 5",s3.intersection(s5))
print("intersection 4 y 5",s4.intersection(s5))
# 'isdisjoint'
print("isdisjoint 3 y 4",s3.isdisjoint(s4))
print("isdisjoint 4 y 5",s4.isdisjoint(s5))
# 'issubset'
print("issubset 3 y 4",s3.issubset(s4))
# 'issuperset'
print("issuperset 3 y 5",s3.issuperset(s5))
# 'intersection_update'
print("intersection_update 3 y 4",s3.intersection_update(s4))
print("Nuevo S3",s3)
# 'pop'
print("pop",s3.pop())
print("pop",s4.pop())
print("pop",s5.pop())
# 'symmetric_difference'
print("symmetric_difference",s3.symmetric_difference(s4))
print("symmetric_difference",s3.symmetric_difference(s5))
# 'symmetric_difference_update'
print("symmetric_difference_update",s3.symmetric_difference_update(s5))
print("new s3",s3)
# 'union'
print("union",s4.union(s5,s3))
# 'update
s6 = set(texto.split())
print("update",s6.update(s3))
detailArchZip(s3)
detailArchZip(s4)
detailArchZip(s5)
detailArchZip(s6)