class Persona:
    def __init__(self): #se lo llama metodo uniger
        self.nombre = "orlando"
        self.apellido = "zelada"
        self.edad = 20


#se le asigna el la clase persona a una variable para guardar su valor
persona1 = Persona()

#se imprime sus datos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)