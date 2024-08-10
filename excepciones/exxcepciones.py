
#Creando funcion que suma numeros
def sumar_dos():
   
   #Iniciando un bucle
    while True:
        #Pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        
        #Si lanzo una excepcion, pedirle que reingrese los datos
    
        except ValueError as e:
            print(f"Error: {e}")
            print("Debes proporcionar unicamente numeros")
            
        #Si todo salio bien terminamos le bucle
        else:
            break
    #Retornando el resultado        
    return resultado

print (sumar_dos())