with open ("archivos\\texto_de_Zaira.txt", "w") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("jajajajajaja no entendi el chiste")
    
    
    #agregando 2 lineas con writelines
    archivo.writelines(["Hola chico como andas?\n", "Plenitud\n"])
    
    #agregando otras 2 lineas
    archivo.writelines(["Juegos de Hambre\n", "Paro\n"])
   