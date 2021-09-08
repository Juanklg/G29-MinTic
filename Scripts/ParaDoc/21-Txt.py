print("Txt".center(60,'-'))

ruta = r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\DataBase\\'



# print("Abre como nuevo".center(60,'-'))
# Abienrto en modo escritura
# nombres = open(ruta,'w')


# nombres = open(ruta,'r')
# Abienrto en modo lectura
# print(nombres.read())

# print("Abre Para añadir texto".center(60,'-'))
# Abienrto en modo añadir texto
# nombres = open(ruta,'a')
print("Escribir texto".center(60,'-'))
data = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5"]
fic = open(ruta+'w.txt', "w",encoding='utf8')
for line in data:
    fic.write(line)    
    fic.write("\n")
fic.close()

print("Leer texto".center(60,'-'))
fic = open(ruta+'w.txt', "r",encoding='utf8')
print(fic.read())
fic.close()

print("Leer linea a linea".center(60,'-'))
fic = open(ruta+'w.txt', "r",encoding='utf8')
lines = []
for line in fic:
    lines.append(line)
fic.close()

print(lines)
lines1 = [s.rstrip('\n') for s in lines]
print(lines1)


