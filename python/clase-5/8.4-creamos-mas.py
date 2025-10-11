class persona:
    def __init__(self, nombres, edad, sexo):
        self.nombres = nombres
        self.edad = edad
        self.sexo = sexo

per1 = persona("zelada", 20, "masculino")
per2 = persona("gordo", 11, "masculino")

print(f"esta el la persona 1: {per1.nombres} {per1.edad} {per1.sexo}")
print(f"esta es la persona 2: {per2.nombres} {per2.edad} {per2.sexo}")