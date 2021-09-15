import pandas as pd

def casos(ruta_archivo: str)-> dict:
    Diccionario1 = {}
    Diccionario2 = {}
    Diccionario3 = {}
    df = pd.read_csv(ruta_archivo)
    
    df = df.sample(30)
    dep=df['Departamento o Distrito']
    edades=df['Edad']
    dic2 = pd.concat([dep, edades], axis = 1)
    print(dic2)

    # print(dic2.groupby('Departamento o Distrito')['Edad'])
    
    
    vl = dep.value_counts()
    print(vl)
    # mean_df = r.mean()
    # print(mean_df)



    
    
    
    return [Diccionario1, Diccionario2, Diccionario3]

print(casos(r'C:\Users\MakeDream\Desktop\Ruta1\G29-MinTic\DataBase\csv\Casos_positivos_de_COVID-19_en_ColombiaDiezMil.csv'))