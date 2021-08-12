#asi se define una funcion
def dentroDelRango(v:int,vm=5,vM=35)->str:
    res = None
    '''
    Ingresa 3 valores
    El valor a validar dentro del rango
    El valor minimo del rango
    El valor maximo del rango
    '''
    dentroRango = v >= vm and v <= vM
    if dentroRango:
        res = 'El valor '+str(v)+' está dentro de rango'
    else:
        res = 'El valor '+str(v)+' está fuera de rango'

    return res

#la plataforma del curso se encargara de lo siguiente
#captura el nombre de la fucion y le asigna unos valores para validar q el resultado dela funcion,
# sea el mismo al propuesto en el eneunciado

#valores de ejemplo

v = 6
vm = 2
vM = 20

#la plataforma ejecuta nuestra funccion con los valores de ejemplo q tiene el sistema cargado
res = dentroDelRango(v,vm,vM)

# la plataforma valdia qla res sea igual a la propuesta con lso valores de ejemplo
print(res)
