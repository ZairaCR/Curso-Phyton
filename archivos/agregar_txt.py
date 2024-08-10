with open ("archivos\\texto_de_Zaira.txt", "a") as archivo:
    
    #usando un blucle para agregar varias lineas 
    
    archivo.write("\n")
    
    for i in range (5):
        #agregando lineas
        archivo.write(f"Linea {i+1} agregando lineas con append\n")
    