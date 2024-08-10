#abriendo el archivo con with open 
with open ("archivos\\texto_de_Zaira.txt") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el contenido
    print(contenido)
    
#no es necesario cerrarlo al usar with open    
    