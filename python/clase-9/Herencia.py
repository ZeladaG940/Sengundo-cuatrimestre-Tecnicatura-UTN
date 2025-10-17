class persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    #getter and setter nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, newnombre):
        self._nombre = newnombre

    #getter and setter edad
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, newedad):
        self._edad = newedad

    #para poder ver los resulatdos se utiliza el metodo __str__, se debe de para si o si un string cadena
    def __str__(self):
        return f"{self._nombre}, {self._edad}"
#Herencia, la clase empleado recibe a persona
class empleado(persona):

    #se le asigna 2 nuevo parametros para la herencia
    def __init__(self, salario, nombre, edad):

        #para traer los datos como erncia se ocupa super
        super().__init__(nombre, edad)
        self._salario = salario

    #getter and setter salario
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, newsalario):
        self._salario = newsalario

    def __str__(self):
        return f"estos son los datos: {self._salario}, {super().__str__()}" #super().__str__() trae el mismo metodo de la clase padre
per1 = empleado(1400, "zelada", 42)
print(per1.nombre)
print(per1.edad)
print(per1.salario)

#metodos aplicados
per1.nombre = "Arturo"
per1.edad = 18
per1.salario = 400
print(per1.nombre)
print(per1.edad)
print(per1.salario)