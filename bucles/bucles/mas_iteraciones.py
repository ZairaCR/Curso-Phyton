#creando las listas
frutas = ["bananas", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola Zai"
numeros = [2, 5, 8, 10]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")
    
#evitar que el bule se siga ejecutando
for fruta in frutas:
    print(f"me voy a comer un {fruta}")
    if fruta == "pera":
        break
else:
    print("terminamos con todas las frutas")
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo (duplicamos un numero)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)