class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if self.enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"

miCoche = Coche()

print("El largo del coche es:", miCoche.largoChasis)
print("El coche tiene:", miCoche.ruedas, "ruedas")

miCoche.arrancar()

print(miCoche.estado())

print("**********************************************************")

miCoche2 = Coche()
print("El largo del coche es:", miCoche2.largoChasis)
print("El coche tiene:", miCoche2.ruedas, "ruedas")
print(miCoche2.estado())
