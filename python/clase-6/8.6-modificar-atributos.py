class persona:
    def __init__(self, nombre, sexo, edad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

per1 = persona("zelada", "masculino", 20)

print(f"este es el objeto 1 = {per1.nombre} {per1.edad} {per1.sexo}")

#asi se modifica los atributos
per1.nombre = "Uwu"
per1.sexo   = "dinosaurio"
per1.edad   = 50

print(f"este es el objeto 1 pero modificado = {per1.nombre} {per1.edad} {per1.sexo}")