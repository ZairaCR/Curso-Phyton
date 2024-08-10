#2 listas, una con nombres otra con apellidos
nombres = ["Zaira","Luis","Cecilia","Gabriela","Gerardo"]
apellidos = ["Cruz","Garcia","Ramirez","Luna","Torres"]

#Registrar esta informacion en un txt de forma optima

with open("archivos_problemas\\nombres_y_apellidos.txt","w") as  arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellidos: {a}\n----------\n") for n,a in zip(nombres,apellidos)]
    
