
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [52, 16, 14, 72]

#recorriendo la lista animales 
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')
    
#recorriendo la lista numeros y multiplicando cada valor por 10 
for numero in numeros:
    resultado = numero *10
    print(resultado)
    
#iterando dos listas del mismo tamano al mismo tiempo
for numero, animal in zip(animales,numeros):
    print(f"recorriendo lista1: {numero}")
    print(f"recorriendo lista2: {animal}")
    

for num in range(5, 8):
    print (num)

#forma no optima de recorrere una lista (no funciona para conjuntos)
for nume in range(len(numeros)):
    print(numeros[nume])
    
#forma correcta de recorrer una list con su indice
for nume, i in enumerate(numeros):
    print(f"el indice es: {nume} y el numero: {i}")
    
#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
#Todo lo visto funciona para listas, tuplas y conjuntos
