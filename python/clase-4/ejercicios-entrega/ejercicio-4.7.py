#ejercicio 2:
#modificar los elemntos de una lista
#llenar una lista con numeros de 1 al 10, luego modificar los elementos de la lista multiplicandolos
#por un valor ingresado por el usuario

#se ingresa los valores a la lista
lista = []
i = 0
while i<10:
    lista.append(i)
    i+= 1
print(lista)

mult = int(input("ingrese el valor a  multiplicar cada valor: "))

#se mustiplica cada valor de la lista por un numero ingreado por el usuario
for i in lista:
    i *= mult
    print(i, end="-")