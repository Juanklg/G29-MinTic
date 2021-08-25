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
