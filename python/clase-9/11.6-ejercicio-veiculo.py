#class Vehiculo:
#Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo.
# La clase padre debe tener los siguientes atributos y métodos:
#Vehiculo (clase padre)
#-Atributos(color, ruedas)
#-Métodos(__init__(color, ruedas) y _str__())
#Auto(clase hija de Vehiculo)
#-Atributos(velocidad (km/hr))
#-Métodos(_init__(color, ruedas, velocidad) y_str__())
#Bicicleta(clase hija de Vehiculo)
#-Atributos(tipo(urbana/montaña/etc.)
#-Métodos(__init__(color, ruedas, tipo) y _str__()
#Crear un objeto de cada clase

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f" color: {self.color} , ruedas: {self.ruedas}"


class auto(Vehiculo):
    def __init__(self, velocidad, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return f"{self.velocidad} k/h, {super().__str__()}"


class bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"tipo: {self.tipo} , {super().__str__()}"

#clase padre
ob = Vehiculo("rojo", 4)
print(ob)

#objeto herencia auto
ob2 = auto(5, "verde", 2)
print(ob2)

#objeto herencia bicileta
ob3 = bicicleta("depotiva", "azul", 2)
print(ob3)