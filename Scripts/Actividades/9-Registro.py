print("Para el registro se solictan los siguientes datos")
nombre = input("Ingrese nombre :")
edad = input("Ingrese edad (debe ser en numeros) : ")
altura = input("Ingrese altura (en numeros) : ")
rolAdmin = input("Ingrese rol Administrador True/False : ")

try:    
    edad = int(edad)
    altura = float(altura)
    #convirtiendo nuestro ingreso en la variable rolAdmin a Booleano
    if rolAdmin=="True" or rolAdmin=="False":
        if rolAdmin == "True" : rolAdmin=True
        elif rolAdmin == "False" : rolAdmin=False
    else:
        #como no se cumplio la condicionforzo el erro y lanza la except
        exit()
    
#si no lanza ningun error continua el codigo normal
#si lanza algun error retorna el bloque de codigo despues del except
except:
    print("Alguno de los valores ingresados no es correcto")
    print("vuelva a correr la aplicacion")
    #le damos fin a la aplicacion por error del usuario
    exit()

print(f''' Registro Exitoso
    Nombre = {nombre}
    Edad = {edad}
    Altura = {altura} metros
    Administrador = {rolAdmin}
''')

if rolAdmin==True:
    print("El usuario no puede ser administrador entonces cambieremos su rol")
    rolAdmin = not rolAdmin
    print(f''' Registro actualizado
        Nombre = {nombre}
        Edad = {edad}
        Altura = {altura} metros
        Administrador = {rolAdmin}
    ''')
