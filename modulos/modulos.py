#Immportando un modulo y asignando el nombre "m_salud"
#import modulo_saludar as m_saludar

#desde ese modulo, importamos dos funciones y cambiamos el nombre de despedir
from modulo_saludar import saludar, despedir as adios

#creamos la variable para el resultado
saludo = saludar("Zaira")

#mostramos resultados
print(saludo)
print(adios("Chucho"))

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)

