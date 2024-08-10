#creando una funcnion que nos devuelva los numeros primos 
#entre 0 y el argumento que pasamos

#creando una funcion que verifique si un numero es primo
def es_primo(num):
    
    #verificamos que el nuero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num-1):
        #si es divisible por alguno, retornamos false y termina el bucle
        if num%i==0: return False
        #si termina elbucle, significa que no fue divisivle entonceses primo 
    return True

#creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creando la lista
    primos = []
    for i in range(3, num+1):
        #
        resultado = es_primo(i)
        if resultado ==  True:
            primos.append(i)
    return primos
        

resultado = primos_hasta(100)
print(resultado)