#definimos nuestra funcion
def sumaSimple(n1:int,n2:int) -> int:
    res = n1 + n2
    return res

def funcionSinArgs() :
    print("Aca empieza la funcion")
    print("Aca termina la funcion")

def probandoPass(): pass

def repetir_funciones():
    print("corriendo repetir funciones")
    imprime_cosas()
    imprime_cosas()

def imprime_cosas():
    print("Cosa 1")
    print("Cosa 2")

def BeneficiosOPerdidas(ingresos:int,gastos:int=1000000):
    """
    Esta funcion me calcula si hay ganacias o perdidas
    Basado en los ingresos y los gastos totales
    Ingresos y los gastos deben ser e typo int
    """
    print(f"Ingresos = {ingresos}")
    print(f"Gastos = {gastos}")
    if ingresos > gastos:
        valorResultado = ingresos-gastos
        resultado = "Ganancia = "+str(valorResultado)
    elif ingresos == gastos:
        valorResultado = gastos-ingresos
        resultado = "Sin ganacias ni perdidas"
    else:
        valorResultado = gastos-ingresos
        resultado = "Perdida = "+str(valorResultado)
    return [resultado,valorResultado]

ingresos = 5000
gastos = 2000

funcionSinArgs()
resultadoSuma = sumaSimple(7, 5)
repetir_funciones()

print(BeneficiosOPerdidas(3000))
print(BeneficiosOPerdidas(3000, 7000))
res = BeneficiosOPerdidas()
print(res[1])