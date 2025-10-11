class persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    #creacion de nuevo metodos
    def mostrar_detalle(self):
        #solo imprime
        print(f"se imprimen los nombres los atributos: {self.nombre} {self.edad} {self.sexo}")


#se agregan los atributos
per1 = persona("zelada", "masculino", 20)

#se imprimen los datos
per1.mostrar_detalle()