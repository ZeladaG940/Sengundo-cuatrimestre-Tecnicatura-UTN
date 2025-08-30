#en una lista pueden aver muchos tipos de datos
lista = []
lista.append(1)
lista.append("micha")
lista.append(True)
lista.append(1.0)
lista.append(2)
print(lista)

#se puede concatenar listas
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = lista1 + lista2
print(lista3)

#como agregar varios elemtos a una lista
lista4 = []
lista4.extend([1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(lista4)

#como saber en que indice esta un valor ingresado
print(lista4.index(3))

#como saber cuantos valores repetidos ahi con el numero ingresado
print(lista4.count(1))

#como poner enm reversa una lista
lista4.reverse()
print(lista4)

#como multiplicar una lista
lista4 *= 2
print(lista4)

#como poner en orden una lista
lista4.sort()
print(lista4)