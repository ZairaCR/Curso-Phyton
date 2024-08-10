
#forma no optima de sumar valores

#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados+ numero
#    return numeros_sumados

#resultado = suma([5, 3, 9])

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resulta = suma_total([10, 20, 40, 55, 5])
print(resulta)

#lo mismo que arriba pero utilizando el operador * como argumento (*args)
def suma(nombre,*numeros):
    return f"{nombre} la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Zaira", 5, 3, 9)



