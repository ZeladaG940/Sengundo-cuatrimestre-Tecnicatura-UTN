class persona:
    def __init__(self, nombre, edad, ciudad):
        self._nombre = nombre
        self._edad   = edad
        self._ciudad = ciudad

    def mostrar(self):
        print(f"los datos son: {self.nombre} {self.edad} {self.ciudad}")

    def __del__(self):
        print(f"se elimino {self.nombre} {self.edad} {self.ciudad}")

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def ciudad(self):
        return self._ciudad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad

if __name__ == "__main__":
    per1 = persona("Gira", "Mendoza", "Tupungato")
    per1.mostrar()
    per1.nombre = "owo"
    per1.apellido = "app.js"
    per1.edad = 18
    per1.mostrar()

    per2 = persona("Esteban", "torta", "Mauipu")
    per2.mostrar()
    per2.nombre = "kasdsal"
    per2.apellido = "lllll"
    per2.edad = 40
    per2.mostrar()