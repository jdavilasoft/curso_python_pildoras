class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        
        if self.__enMarcha:
            chequeo = self.__chequeo_interno()

        if self.__enMarcha and chequeo:
            return "El coche esta en marcha"
        elif self.__enMarcha and chequeo == False:
            return "Chequeo no superado, no podemos arrancar"
        else:
            return "El coche esta detenido"

    def estado(self):
        print("El coche tiene,", self.__ruedas, "un ancho de", self.__anchoChasis, "y un largo de:", self.__largoChasis)
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "OK"
        self.aceite = "mal"
        self.puertas = "Cerradas"

        if (self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="Cerradas"):
            return True
        else:
            return False

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("**********************************************************")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()