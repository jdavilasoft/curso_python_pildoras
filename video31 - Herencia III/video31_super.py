class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = lugar_residencia

    def describir(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Residencia:" ,self.residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, emp_nombre, emp_edad, emp_residencia):

        super().__init__(emp_nombre, emp_edad, emp_residencia)

        self.salario = salario
        self.antiguedad = antiguedad

    def describir(self):

        super().describir()
        print("Salario:", self.salario, "Antiguedad:", self.antiguedad)

Antonio = Empleado(1500, 15, "Antonio", 55, "Espania")
Antonio.describir()

# Saber si el objeto es instancia de una clase
print(isinstance(Antonio, Empleado))
print(isinstance(Antonio, Persona))