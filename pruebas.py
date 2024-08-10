cantidad_alumnos = 4
alumnos = []
for i in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    alumno = (nombre, edad)
    alumnos.append(alumno)
alumnos.sort(key=lambda x:x[1])
    
asistente = alumnos[0][0]
profesor = alumnos[cantidad_alumnos -1][0]
    
    
print(asistente)
print(profesor)