#Crenado mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")
    
#Lanzando mi propia exceptiom
#raise MiExcepcion("jajajajaja")

#manejandola
try:
    raise MiExcepcion("jajajajaja")
except:
    print("Como vas a cometer ese error?")
