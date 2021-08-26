import crud
from datetime import datetime
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

def printMenu(el):
    print('---------------------------------')    
    for i,e in zip(range(1,len(el)+1),el):
        print(f"\t{i} - {e}")

def menuOriginal(rut):
    datosActualizados = {
        'titulo':'',
        'descripcion':'',
        'estado':'',
        'fechaInicio':'',
        'fechaFinalizacion':'',
    }
    while True:
        print('Indique la accion que desea realizar: ')
        print('\t 1-Consultar')
        print('\t 2-Actualizar')
        print('\t 3-Crear nueva tarea')
        print('\t 4-Borrar')
        accion = input('Escriba la opccion: ')

        if not(accion=="1") and not(accion=="2") and not(accion=="3") and not(accion=="4"):
            print('Comando invalido por favor eliga una opcion valida')
        elif accion=='1': 
            opc_consulta='' 
            print('Indique las tareas que desea consultar: ') 
            print('\t 1-Todas las tareas') 
            print('\t 2-En espera') 
            print('\t 3-En ejecucion') 
            print('\t 4-Por aprobar') 
            print('\t 5-Finalizada') 
            opc_consulta = input('Digite las tareas que desea consultar: ')
            print("Consulta",opc_consulta)
            if opc_consulta=='1': 
                print() 
                print() 
                print('* Consultando todas Las tareas *') 
                crud.leer(rut, 'todo') 
            elif opc_consulta=='2': 
                print() 
                print() 
                print('* Consultando tareas en espera *') 
                crud.leer(rut, 'En espera') 
            elif opc_consulta=='3': 
                print() 
                print() 
                print('* Consultando tareas en ejecucion *') 
                crud.leer(rut, 'En ejecucion') 
            elif opc_consulta=='4': 
                print() 
                print() 
                print('* Consultando tareas por aprobar *') 
                crud.leer(rut, 'Por aprobar') 
            elif opc_consulta=='5': 
                print() 
                print() 
                print('* Consultando tareas finalizadas *') 
                crud.leer(rut, 'Finalizada')
        elif accion=='2': 
            datosActualizados={'titulo':'', 'descripcion':'', 'estado':'', 'fecha inicio':'', 'fecha finalizacion':''}
            print('* Actualizar Tarea *') 
            print() 
            id_Actualizar=int(input('Indique el Id de la tarea que desea actualizar: ')) 
            print() 
            print('* Nuevo titulo *') 
            print('*Nota: si no desea actualizar el titulo solo oprima ENTER') 
            datosActualizados['titulo']=input('Indique el nuevo titulo de la tarea : ') 
            print() 
            print('* Nueva descripcion *') 
            print('Nota: si no desea actualizar la descripcion solo oprima ENTER') 
            datosActualizados[ 'descripcion']= input('Indique La nueva descripcion de la tarea : ') 
            print() 
            print('* Nueva estado **') 
            print('En espera: 2') 
            print('En ejecucion: 3') 
            print('Por aprobar 4') 
            print('Finalizada: 5')
            print('**Nota: si no desea actualizar el estado solo oprima ENTER') 
            estadoNuevo= input('Indique el nuevo estado de la tarea : ') 
            if estadoNuevo=='2': 
                datosActualizados['estado']='En espera' 
            elif estadoNuevo=='3': 
                datosActualizados[ 'estado']='En ejecucion' 
            elif estadoNuevo=='4': 
                datosActualizados[ 'estado']='Por aprobar' 
            elif estadoNuevo=='5': 
                now = datetime.now() 
                datosActualizados['estado']='Finalizada' 
                datosActualizados['fecha finalizacion']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year) 
                
            now = datetime.now() 
            datosActualizados['fecha inicio']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year) 
            crud.actualizar(rut,id_Actualizar, datosActualizados) 
            print()
        elif accion=='3': 
            datosActualizados={'tarea':'', 'descripcion':", 'estado':'", 'fecha inicio':'', 'fecha finalizacion':''} 
            print('* Crear nueva Tarea *') 
            print() 
            print('* titulo *') 
            print() 
            datosActualizados['titulo']=input('Indique el titulo de la tarea : ')
            print() 
            print('* descripcion *') 
            datosActualizados['descripcion']= input('Indique la descripcion de la tarea : ')
            print() 
            datosActualizados['estado']='En espera' 
            now = datetime.now() 
            datosActualizados['fecha inicio']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year) 
            datosActualizados['fecha finalizacion']=''
            crud.agregar(rut, datosActualizados) 
        elif accion=='4': 
            print('') 
            print('* ELiminar Tarea **') 
            iden=int(input('Indique el Id de la tarea que desea eliminar: '))
            crud.borrar(rut, iden)
