#si el modulo esta dentro de una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("C:\\Users\\michz\\OneDrive\\Escritorio\\Curso Python\\funciones_buenas")
print(sys.path)

import saludar as modulo_saludar

print(modulo_saludar.saludar("Paola"))