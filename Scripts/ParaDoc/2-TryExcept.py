numero = 61
#los input(los input's siempre seran de type 'str',texto,string)
#capturamos el ingreso total y lo almacenamos en x
x = input("Ingrese x (debe ser en numeros) : ")
#capturamos el gasto total y lo almacenamos en y
y = input("Ingrese y (debe ser en numeros) : ")


#hacemos pruebas de un codigo y verificamos que no lanza ningun error
try:
    x=int(x)
    y=int(y)    
    #si no lanza ningun error continua el codigo normal
#si lanza algun error retorna el bloque de codigo despues del except
except:
    print("El valor ingresado debe ser de tipo numerico o de type int")
    print("vuelva a correr la aplicacion")
    #le damos fin a la aplicacion por error
    exit()

print("El tyr funciono de forma correcta")