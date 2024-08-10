#falto el profe y los alumnos armaran la clase

#pedir el nombre y la edad de los alumnos que asistieron hoy

#funcion para obtener al asistente y al profesor segun la edad.
def obtener_alumnos(cantidad_alumnos):
    
    #creando la lista con los calumnos
    alumnos = []
    
    #ejecutando un for para pedir informacion de cada alumno
    for i in range(cantidad_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        alumno = (nombre, edad)
        
        #agregando la informacion a la lista
        alumnos.append(alumno)
        
    #ordenandolos de menor a mayor segun su edad    
    alumnos.sort(key=lambda x:x[1])
    
    #alumnos[x] devuleve una tupla con (combre, edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = alumnos[0][0]
    profesor = alumnos[-1][0]
    
    #reotrnamos una tupla
    return asistente, profesor

#desempaquetamos lo que nos retorna la funcion 
asistonto, profe = obtener_alumnos(4)

#mostramos el resultado
print(f"el profesor sera: {profe} y el asistente sera: {asistonto}")
    
    

    