def detailVar(var:any):
    print("El valor es :",var)
    print("Es de tipo :",type(var))
    print("Su longitud es :",len(var))
    for x in var:
        # if x==7:break
        print("El valor que toma x en el for es :",x)
    return 

def printIndex(iterable):
    for x in range(0,len(iterable)):        
        print("La pos: {0} tiene el valor: {1}".format(x , iterable[x]))

var = range(3)
detailVar(var)
var = range(5,10)
detailVar(var)
var = range(0,10,2)
detailVar(var)