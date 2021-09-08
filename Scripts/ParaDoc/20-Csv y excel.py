import pandas as pd

print("CSV".center(60,'-'))
data = {
    'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
    'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
    'age': [27, 31, 36, 53, 48, 36, 40, 34],
    'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
    'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
}

datos = {"manzanas":[3,2,0,1],"naranjas":[0,3,7,2]}
compras = pd.DataFrame(datos,index=['Mateo','Kevin','Juan','Wendy'])
compras.name = "Ventas Prueba"
compras.index.name = 'Clientes'
compras.columns.name = "Frutas"

print("Creando CSV con data".center(50,'-'))
datosDataFrame = pd.DataFrame(data)

print(datosDataFrame)
print("Clase".center(60,'-'))
print(compras)

datosDataFrame.to_csv('example.csv')
compras.to_csv('compras.csv',sep='-')

print("leyendo CSV y creando DF".center(50,'-'))
df = pd.read_csv('compras.csv',sep='-')
print(df)

df2 = pd.read_csv('example.csv')
print(df2)

print("leyendo CSV y usando atributos".center(50,'-'))
df3 = pd.read_csv('compras.csv',
                    sep='-',
                    index_col='Clientes'
                    )
df4 = pd.read_csv('example.csv',
                    skiprows=1,
                    header=None,
                    names=['UID', 'First Name', 'Last Name', 'Age', 'Sales #1', 'Sales #2'],
                    index_col='UID',
                    na_values='?'
                    )

print(df3)
print("*".center(50,'-'))
print(df4)

print("Crear Excel".center(50,'-'))
df3.to_excel(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\DataBase\xcompras.xlsx',sheet_name='compras')
# df3.to_excel(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\DataBase\Xexample.xlsx',sheet_name='compras')
df4.to_excel(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\DataBase\Xexample.xlsx',sheet_name='ejemplo')

print("read Excel".center(50,'-'))
ruta = r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\DataBase\dbTask.xlsx'
df = pd.read_excel(ruta,sheet_name='Datos del crud',names=['ID','Titulo', 'Descripcion','Estado','Fecha inicio' , 'Fecha finalizado',  'Unnamed'],index_col='ID')
df.pop('Unnamed')
print(df)

