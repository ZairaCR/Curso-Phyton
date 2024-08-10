#usando open para brir un archivo
archivo = open("archivos\\texto_de_Zaira.txt")

#leer el archivo completo
archivo = archivo.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea 
#linea = archivo.readline()

#cerrar el alchivo
archivo.close()

print(archivo)


