class persona:
    def __init__(self, nombre, edad, sexo):#esto resive los argumentos de clase
        self.nombre = nombre
        self.edad   = edad
        self.sexo   = sexo

per1 = persona("orlando", 20, "masculino") #estos son los argumentos que se le envia ala clasee

#asi se imprime cada argumento de la clase
print(per1.nombre)
print(per1.edad)
print(per1.sexo)