#creando un conjunto con set
conjunto  = set(["Dato 1", "Dato 2"])

#metiendo un conjunto entro de otro 
# conjunto
conjunto1 =frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

#teoria de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1 
print(resultado)

#verificando si es un subconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1 
print(resultado)

##verificar si hay algun numero en comun, de haberlo deveulve false,
#de no haber ningun numero en comun devuelve true
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)

