numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#creando una funcion lambda para multiplicar una funcion por dos
multiplicar_por_dos = lambda x : x*2

#creando funcion cmomun que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True
    
#usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)

#creando lo mismo que antes pero con lambda
numeros_pares_lambda = filter(lambda numero:numero%2== 0, numeros)

print(list(numeros_pares_lambda))