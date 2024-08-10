#crea una lista con list()
lista = list(["hola", "adios", 40721, True])
lista2 = [18, 21, 2021, 2003, 20, 7, 10, True, False]

#devuelve la cadena de elementos de la lista
cantidad_elementos = len(lista)
print(cantidad_elementos)

#agregando un elemento a la lista
lista.append("JAJAJAJAJAJA")
print(lista)

#agregando un elemento a la lista en una posicion especifica, recorre los demas
lista.insert(2, "mama")
print(lista)

#agregando varios elementos a la lista
lista.extend([False, 2024])
print(lista)

#eliminando un elemento de la lista (por su indice) 
# para eliminar el ultimo se usa (-1), eliminar el penultimo(-2)
lista.pop(5)
print(lista)

#removiendo un elemento de la lista por su valor, en caso de no encontrarlo salta error
lista.remove("mama")
print(lista)

#eliminando todos los elementos de la lista
#lista.clear


#invirtiendo los elementos de una lista
lista.reverse()
print(lista)


#ordena una lista del menor al mayor, 
lista2.sort()
print(lista2)
#si usamos el parametro reverse=True lo ordena en reversa
lista2.sort(reverse=True)
print(lista2)

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index("hola")
print(elemento_encontrado)



