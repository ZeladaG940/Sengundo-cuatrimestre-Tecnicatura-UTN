#ejercicio 1: crear una funcion para sumar los valores recibidos de tipo
#numerico, utilizando argumentos variables *arg como parametro de la
#funcion y agregar como resultado la suma de todos los valores pasados
#como argumentos

def sumar(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma
print(sumar(1,2,3,4,5,6,7,8,9,10))
