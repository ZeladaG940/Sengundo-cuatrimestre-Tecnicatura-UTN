class persona:
    def __init__(self, nombre, apellido, dni):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
    def mostrar(self):
        print(f"estos osn los metodos a mostrar: {self._nombre} {self._apellido} {self._dni}")

    #como crear un metodo getter
    @property
    def nombre(self):
        print("estamos usuando el metodo get")
        return self._nombre

    #y para crear un metodo setter que depende el getter
    @nombre.setter
    def nombre(self, nombre):
        print("estamos usuando el metodo set")
        self._nombre = nombre

#como usar el metodo get
per1 = persona("uwu", "owo", 49)
per1.mostrar()
print(per1.nombre)

#como usar el metodo set
per1.nombre = "zelada"