print("Txt".center(60,'-'))

ruta = r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\DataBase\txt\\'

def leerTxt(archivo:str):
    print(f"Leer texto {archivo}".center(60,'-'))
    fic = open(ruta+archivo,'r',encoding='utf8')
    lines = fic.readlines()
    lines = [s.rstrip('\n') for s in lines]
    fic.close()
    return lines

def crearTxt(nombre:str):
    print(f"Crear txt {nombre}".center(60,'-'))
    file=open(ruta+nombre+'.txt','w')
    file.close()

def actualizarTxt(file:str,data:list):
    print(f"Actuaizar txt {file}".center(60,'-'))
    file=open(ruta+file,'a',encoding='utf8')
    file.writelines('%s\n' %s for s in data)
    file.close()

def agregarLineaTxt(file:str,linea:str):
    print(f"Agregar liena a txt {file}".center(60,'-'))
    file=open(ruta+file,'a',encoding='utf8')
    print(linea,file=file)
    file.close()

leido = leerTxt('w.txt')
print(leido)
crearTxt('tareas')
actualizarTxt('tareas.txt',leido)
agregarLineaTxt('tareas.txt','una mas')