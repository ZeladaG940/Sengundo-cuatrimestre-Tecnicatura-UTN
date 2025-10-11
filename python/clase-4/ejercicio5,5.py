#as una tabla de multiplicar que muestre toda su tabla asta el 10
numero = int(input("ingrese el numero para saber su tabla: "))
for i in range(1, 11, 1):
    result = numero * i
    print(f"{numero} * {i} = {result}")