cadena2 = "hola soy Zaira"
cadena1 = "Bienvenido fiera"
cadena3 = "04072021"
cadena4 = "Zaira.Paola.Cruz.Ramirez"

#convertir a mayusculas
mayusc = cadena1.upper()
print(mayusc)

#convertir a minusculas
minusc = cadena1.lower()
print(minusc)

#primera letra en mayuscula y todas las demas a minuscula
primer_mayusc = cadena2.capitalize()
print(primer_mayusc)

#buscamos una cadena en otra cadena, de no encontrarse devuelve -1
busqueda_find = cadena2.find("soy")
print(busqueda_find)

#buscamos una cadena en otra cadena, de no encontarse manda un error
busqueda_index = cadena2.index("a")
print(busqueda_index)

#si es numerico devuelve true, sino devuelve false
es_numerico = cadena3.isnumeric()
print(es_numerico)

#si es alfanumerico devuelve true, sino devuelve false 
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("ie")
print(contar_coincidencias)

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)
print(contar_caracteres)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("Bienv")
print(empieza_con)

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("ra")
print(termina_con)

#remplaza un pedazo de la cadena dada, con otra dada
cadena_nueva = cadena1.replace("e", "zaira")
print(cadena_nueva)

#separar cadenas con la cadena que le pasemos, devuelve una lista 
cadena_separada = cadena4.split(".")
print(cadena_separada)
print(cadena_separada[2]) #al ser una lista se puede mostrar cada elemeto de la lista por su indice



