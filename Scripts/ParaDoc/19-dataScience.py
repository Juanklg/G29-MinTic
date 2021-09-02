import pandas as pd




print("Creando una Serie de forma convencional".center(60,'-'))
ven = pd.Series([15,28,97],index=["Ene","Feb","Mar"])
print(ven)
print("Caracteristicas".center(60,'-'))
print(ven[0])
print(ven[2])
print(ven[1])
print(ven['Mar'])
print(ven['Ene'])
print(ven['Feb'])
print(ven.dtype)
print(ven.axes)
print(ven.shape)

print("Accediendo a valores y indices".center(60,'-'))
print(ven.values)
print(ven.index)

print("Asignando name".center(60,'-'))
ven.name = "Ventas Prueba"
ven.index.name = 'Meses'

print("DataFrames".center(60,'-'))
#crear dict para compras
datos = {"manzanas":[3,2,0,1],"naranjas":[0,3,7,2]}
#asignamos el dict a el constructor del data frame
compras = pd.DataFrame(datos)

compras = pd.DataFrame(datos,index=['Mateo','Kevin','Juan','Wendy'])
print("DF Index".center(60,'-'))
print(compras.index)
print(compras.columns)
print(compras.axes)
compras.name = "Ventas Prueba"
compras.index.name = 'Clientes'
compras.columns.name = "Frutas"
print(compras)
print("DF values".center(60,'-'))
print(compras.values)
print(compras.values.shape)

print("Serie desde diccionario".center(60,'-'))
d = {'Mar':8,'Ene':6,'Feb':1}
s= pd.Series(d)
print(s)
print("".center(60,'-'))
s2 = pd.Series(d,index={"Mar","Feb","Ene"},dtype=int)
print(s2)

print("DataFrames desde diccionario".center(60,'-'))
uni = [
    {"Ag":2, "Au":5, "Cu":3, "Pt":2},
    {"Ag":4, "Au":6, "Cu":7, "Pt":2},
    {"Ag":3, "Pb":2, "Cu":4, "Pt":1}
]
unidades = pd.DataFrame(uni,index=[2015,2016,2017])
print(unidades)