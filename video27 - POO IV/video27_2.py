class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        
        if self.enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"

    def estado(self):
        print("El coche tiene,", self.ruedas, "un ancho de", self.anchoChasis, "y un largo de:", self.largoChasis)
        

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("**********************************************************")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
