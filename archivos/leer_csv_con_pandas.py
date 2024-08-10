import pandas as pd

#usando la funcion read_csv para leer un archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["Nombre"]

#acceder a varios elementos de la cadena
#cadena = "0123456789"
#print(cadena[1:8])

#ordenar el dataframe por edad
df_orden_ascendente = df.sort_values("Edad")

#ordenandolo de forma descendesnte
df_orden_descendete = df.sort_values("Edad",ascending=False)

#concantenando los dos dataframes
df_concatenados = pd.concat([df,df2])

#accediendo a las primeras 3 fila con head()
primeras_fila = df.head(3)

#accediendo a las ultimas 3 fila con tail()
ultimas_fila = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape()
filas_y_columnas_totales = df.shape
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]

#Con desempaquetado mas simple
filas_totales, columnas_totales = df.shape

#obteniendo data de estadistica del dataframe
df_info= df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"Edad"]

#accediendo a un elemento especifico del df con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 20
mayor_que_20 = df.loc[df["Edad"]>20,:]


print(mayor_que_20)



