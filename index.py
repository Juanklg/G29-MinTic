# import funciones
# print(dir(funciones))
from funciones import isLogin, menuOriginal
# from funciones as fn

import crud

isLogin("Login")
#------------------------------------------------------
## solo se ejecuta esto si el usuario es = 'Login'
print("Inicia la App")

rut = r"C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\dbTask.xlsx"
menuOriginal(rut)








# task = {"Nombre","Descripcion","Estado","Inicio","Fin"}
# opciones = ("Create","Read","Update","Delete","Exit")
# filterState = ["Todas","Pendientes","Ejecucion","Revision","Finalizada"]
# menuState = filterState[1:]

# while True:
#     opcion=''
#     print('---------------------------------')
#     printMenu(opciones)
#     opcion=input('Digite la opcion deseada: ')
#     print("\nUsted selecciono la opcion",opcion)
#     if not(opcion=="1") and not(opcion=="2") and not(opcion=="3") and not(opcion=="4") and not(opcion=="5"):
#         print("Comando Invalido")
#     elif opcion=="1":#Create
#         dictTask=dict.fromkeys(task)        
#         print('\n* Crear nueva Tarea *')

#         print('\n* Nombre *') 
#         dictTask['Nombre']=input('Indique el Nombre de la tarea : ')

#         print('\n* Descripcion *') 
#         dictTask['Descripcion']= input('Indique la descripcion de la tarea : ')

#         dictTask['Estado']='Pendientes'
#         now = datetime.now()
#         dictTask['Inicio']=str(now.day) +'/'+ str(now.month) +'/'+str(now.year)
#         dictTask['Finalizada']=''
#         crud.Create(rut, dictTask)
#     elif opcion=="2":#Read
#         printMenu(filterState)
#         opcion=input('\nIndique la lista de tareas que quiere revisar: ')
#         print("\nUsted selecciono la opcion",opcion)
#         if not(opcion=="1") and not(opcion=="2") and not(opcion=="3") and not(opcion=="4"):
#             print("Comando Invalido")
#         elif opcion=="1":
#             print('* Consultando Todas Las tareas*') 
#             crud.Read(rut, 'Todas')
#         elif opcion=="2":
#             print('* Consultando las tareas Pendientes*')
#             crud.Read(rut, 'Pendientes')
#         elif opcion=="3":
#             print('* Consultando las tareas Ejecucion*')
#             crud.Read(rut, 'Ejecucion')
#         elif opcion=="4":
#             print('* Consultando las tareas Revision*')
#             crud.Read(rut, 'Revision')
#         elif opcion=="5":
#             print('* Consultando las tareas Finalizada*')
#             crud.Read(rut, 'Finalizada')
#     elif opcion=="3":#update
#         dictTask=dict.fromkeys(task)
#         print('\n* Actualizar Tarea *')
#         id=int(input('Indique el Id de la tarea que desea actualizar: '))

#         print('\n* Nuevo titulo *')
#         print('*Nota: si no desea actualizar el titulo solo oprima ENTER')
#         dictTask['Nombre']=input('Indique el nuevo titulo de la tarea : ')
        
#         print('\n* Nuevo Descripcion *')
#         print('*Nota: si no desea actualizar el titulo solo oprima ENTER')
#         dictTask['Descripcion']=input('Indique la descripcion de la tarea : ')

#         print('\n* Nuevo Estado *')
#         printMenu(menuState)
#         print('*Nota: si no desea actualizar el titulo solo oprima ENTER')        
#         newState = int(input('Indique el nuevo estado de la  tarea : '))
#         dictTask['Estado'] = filterState[newState]
#         if newState == 4:
#             now = datetime.now()
#             dictTask['Fin'] = str(now.day) +'/'+ str(now.month) +'/'+str(now.year)
#         crud.Update(rut,id,dictTask)
#     elif opcion=="4":#delete        
#         print('* ELiminar Tarea **') 
#         id=int(input('Indique el Id de la tarea que desea eliminar: '))
#         crud.Delete(rut, id)
#     elif opcion=="5":exit()