#creando diccionarios con dict()
diccionario = dict(nombre = "Zaira", apellido = "cruz")


#las listas no pueden ser claves y usamos froxenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]) : "jajajaja"}


#creando diccionarios con fromkeys() valor por defecto none 
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionario con fromkeys() cambiando el valor oir defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")



print(diccionario)