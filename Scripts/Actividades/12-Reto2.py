#asi se define una funcion
def dentroDelRango(v:int,vm=5,vM=35)->str:
    res = None
    #esta validacion retorna un true o un false
    dentroRango = v >= vm and v <= vM
    #
    if dentroRango:
        res = 'El valor '+str(v)+' está dentro de rango'
    else:
        res = 'El valor '+str(v)+' está fuera de rango'
    '''
    Ingresa 3 valores
    El valor a validar dentro del rango
    El valor minimo del rango
    El valor maximo del rango
    '''
    return res

#la plataforma del curso se encargara de lo siguiente
#captura el nombre de la fucion y le asigna unos valores para validar q el resultado de la funcion,
# sea el mismo al propuesto en el eneunciado

#valores de ejemplo

# v = 6
# vm = 2
# vM = 20

v = 5
vm = 4
vM = 8

# v = 3
# vm = 5
# vM = 10

#la plataforma ejecuta nuestra funccion con los valores de ejemplo q tiene en el sistema cargado
res = dentroDelRango(v,vm,vM)

print(type(res))

# la plataforma valdia q la res sea igual a la propuesta con los valores de ejemplo y otros valores
print(res)
