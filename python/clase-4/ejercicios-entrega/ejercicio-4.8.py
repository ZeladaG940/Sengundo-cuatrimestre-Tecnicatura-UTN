#ejercicio 3
#insertar elementos y ordenarlos
#pedir elemtos y meterlos en una lista, cuando el usuario introdusca el 0
#el programam dejaria de insertar
#por ultimo le programa mostrara los elementos de menor a mayor

lista = []
cero = False
print("para dejar de ingresar numeros, digite el 0")
while cero == False:

    #optendra los valores y verificara si ingreso el 0
    item = int(input("digite los valores:  "))
    if item == 0:
        cero = True
    else:
        lista.append(item)

lista.sort()
print(lista)