
#Las listas se abren con [], modificable
lista = ["Zaira Cruz", "Soy Dalto", True,1.62]

#Las tuplas se abren con (), pero a diferencia de las listas esta no se puede modificar
tupla = ("Zaira Cruz", "Soy Dalto", True,1.62)

#valido
lista[3] = "Libra"
print(lista[3])

#no valido
#tupla[3] = "Libra"

#Creando un conjunto (set)
#se puede redefinir, mas no modificar
#no se puede acceder por un indice y no almacena datos duplicados
conjunto = {"Zaira Cruz", "Soy Dalto", True,1.62}

#no valido
#print(conjunto[2])

print(conjunto)

#creando un (dict) (la estrctra es key : value y separamos con comas )
diccionario = {
    'nombre': "Zaira Paola", 
    'canal': "soy Dalto", 
    'estas_emocionado': True, 
    'altura': 1.62,
    'dato_duplicado': "soy Dalto"
}

print(diccionario['canal'])

