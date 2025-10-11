import math
#ejercicio 4:
#sacar la raiz cuadrada de un numero positivo
num = int(input("Ingresa un numero: "))

while num < 0:
    print("error el numero deve de ser positivo")
    num = int(input("Ingresa un numero: "))

print(f"la raiz ccuadra de el numero es: {math.sqrt(num)}")
