#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")

#Convertir a string los datos
df['Edad'] = df['Edad'].astype(str)

#mostar el tipo de dato del primer elemento de la columna edad
#print(type(df['Edad'][0])) 

#remplazando los datos por "Garcia"
df['Apellido'].replace("Ramirez","Bustamante",inplace=True)
#print(df['Apellido'])

#eliminando las filas con datos vacios
df = df.dropna()
#Eliminar columnas con datos faltantes (axis=1)
#df = df.dropna(axis=1)


#Elimiar filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante
df.to_csv("archivos_problemas\\datos_limpios.csv")
print(df)