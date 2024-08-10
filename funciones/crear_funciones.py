#creando una funcion simple
#def saludar():
 #   print("Hola Zaira mi reina, como estas?")
    
#ejecutando la funcion simple
#saludar()

#funcion con parametros
def saludar(nombre,sexo):
    sexo = sexo.upper()
    if (sexo == "MUJER"):
        adjetivo = "reina"
    elif (sexo == "HOMBRE"):
        adjetivo = "animal"
    else:
        adjetivo = "maquina"
    
    print(f"Hola {nombre}, Como estas {adjetivo}?")
    
saludar("Zaira","mujer")
saludar("Luis", "Hombre")
saludar("rayo", "nose laverdad")

#crear una funcion que retorne multiples valores
def crear_password_random(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return password, num

#desempaquetando la funcion
contra, primer_num = crear_password_random(398)

#mostrando los resultados obtenidos y los datos utiilizados para obtenerla
print(f"Tu contrasena es: {contra}")
print(f"El numero utilizado para crearla fue: {primer_num}")

