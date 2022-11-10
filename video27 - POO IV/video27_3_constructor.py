class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        
        if self.__enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"

    def estado(self):
        print("El coche tiene,", self.__ruedas, "un ancho de", self.__anchoChasis, "y un largo de:", self.__largoChasis)
        

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("**********************************************************")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
