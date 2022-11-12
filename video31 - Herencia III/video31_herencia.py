class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enMarcha, "\nAcelerando:", self.acelera, "\nFrenando", self.frena)

class Furgoneta(Vehiculo):

    def cargar(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculo):
    hCaballito = ""

    def caballito(self):
        self.hCaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enMarcha, "\nAcelerando:", self.acelera, "\nFrenando", self.frena, "\n", self.hCaballito)

class VElectrico(Vehiculo):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

print("MOTO  ******************************")
miMoto = Moto("Honda", "CBR150")
miMoto.caballito()
miMoto.estado()

print("\nFURGONETA*************************")
miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.cargar(True))

# Herencia múltiple
class BicicletaElectrica(VElectrico, Vehiculo):
    pass

miBicicleta = BicicletaElectrica("Orbea", "TJH")