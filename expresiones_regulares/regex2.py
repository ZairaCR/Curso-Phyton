import re

# La cadena en la que se buscaran los patrones
text = "La fecha es 20/07/1979 y el telefono es +52-999-999-9999"

# El patron a buscar
pattern =  r"\d{2}/\d{2}/\d{4}"

# El texto con el que se remplazara el patron
replacement = "Fecha oculta"

# Remplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern, replacement, text)

# Imprimir el resultado
print("Texto modificado: ", new_text)