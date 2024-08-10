diccionario = {
    "nombre" : "Zaira",
    "apellido": "Cruz",
    "edad": 20
}

#reccoriendo diccionario para obtener las claves
for key in diccionario:
    print(f"la calve es: {key}")
    
#reccoriendo diccionario con items() para obtener las claves y los valores
for key, valu in diccionario.items():
    print(f"la calve es: {key} y el valor es: {valu}")
    