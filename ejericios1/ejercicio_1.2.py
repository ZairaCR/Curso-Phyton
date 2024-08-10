frase = input("Dime una frase para calcular cuanto tardarias si tuvieras que decirla: ")

palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras * 100 //2*0.7 / 100} segundos en decirlo')

if cantidad_de_palabras > 120:
    print("Tranquila reina no te pedi un testamento")