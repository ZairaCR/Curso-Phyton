import re

texto = '''Hola maestro, esta es la cadena 1. como estas mi capitan?
Esta es la linea 234 de texto.
Y Esta es la final (linea 3) definitiva mi capitan'''

#Haciendo una busqueda simple
resultado = re.findall("esta", texto)

#\d -> busca digitos numericos del 0 - 9
resultado = re.findall(r"\d", texto)

#\D -> busca TODO MENOS digitos numericos del 0 - 9
resultado = re.findall(r"\D", texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W", texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\s", texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r"\S", texto)

#. -> busca TODO MENOS saltos de linea
resultado = re.findall(r".", texto)

#\n -> busca saltos de linea
resultado = re.findall(r"\n", texto)

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\.", texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s', texto)


#buscando el principio de una linea
#^ -> busca el comienzo de una linea (buscando hola al principio de la linea)
resultado = re.findall(f'^Hola', texto)

#flags=re.M activa la multilinea 
resultado = re.findall(f'^Esta', texto, flags=re.M)\

#$ -> busca el final de una linea
resultado = re.findall(f'capitan$', texto)

#{n} -> busca n cantidad de veces el valor de la izquierda (esta vez 3 numeros juntos)
resultado = re.findall(r'\d{3}', texto)

#{n,m} -> al menos n, como maximo m 
resultado = re.findall(r'\d{1,4}', texto)

# | -> busca una cosa o la otras
resultado = re.findall(r'\d{1,4}|Hola', texto)
print(resultado)
