#crendo una funcio de tres parametros
def frase (nombre, apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#utilizando keyword arguments
frase_resultante = frase(adjetivo="Lindo", apellido= "Garcia", nombre="Luis")
print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase_tonto(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase = frase_tonto("Michelle", "Cruz", "tonta")
print (frase)