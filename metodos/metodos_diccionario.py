diccionario = {
    "nombre" : 'Zaira',
    "apellido" : "Cruz",
    "edad" : 20
}

#nos devuelve las claves (un objeto dict_item) y tambien sirve para iterar
claves = diccionario.keys()
print(claves)

#get devuelve el valor de una clave, en caso de no encontrar la clave no da error
valor_de_cada_clave = diccionario.get("nombre")
print(valor_de_cada_clave)

#eliminando un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#eliminando todo del diccionario
diccionario.clear()
print(diccionario)