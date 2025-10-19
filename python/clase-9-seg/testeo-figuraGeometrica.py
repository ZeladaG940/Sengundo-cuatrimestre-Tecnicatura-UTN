from hijaCuadrado import *
cuadrado = Cuadrado(7, 9, "azul")
print(f"el area es: {cuadrado.area()}")
print(cuadrado.color)

# MRO = Method Resolution Order
print(Cuadrado.mro())