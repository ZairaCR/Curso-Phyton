#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = round(100 - dalto_curso / otros_cursos_max *100,1)
#diferencia_con_max = 100 - dalto_curso *1000 // otros_cursos_max /10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido
#tiempo_vacio_promedio = 100 - otros_cursos_promedio *1000 // crudo_promedio /10
#tiempo_vacio_dalto = 100 - dalto_curso *1000 // crudo_dalto /10
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio *100
tiempo_vacio_dalto = 100 - dalto_curso / crudo_dalto *100


print("-------------------------------------------------------------------------")
print("El curso de dalto dura:")
print(f' - un {diferencia_con_min}% menos que el mas rapido')
print(f' - un {diferencia_con_max}% menos que el mas lento')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print("-------------------------------------------------------------------------")

print(f'Un curso promedio promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimina {round(tiempo_vacio_dalto, 1)}% de tiempo vacio')
print("-------------------------------------------------------------------------")

#mostrando diferencia si los cursos diraran 10 horas 
print(f'Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio * 10/dalto_curso,1) } horas de otros cursos')
#mostrando diferencia si los cursos diraran 10 horas 
print(f'Ver 10 horas de otros curso equivale a ver {round(dalto_curso * 10/otros_cursos_promedio, 1) } horas de dalto curso')