#listas
lista = ["orlando", "zelada", "gira"]
print(lista)

#como navegar por las listas
print(lista[0])
print(lista[1])

#como mostras los indices de forma celectiva
print(lista[0:2])
print(lista[1:2])

#como modificar el valor de una lista
lista[0] = "perro"
print(lista[0])

#como iterar una lista
for iten in range(0,len(lista)):
    print(lista[iten])

#preguntar cuantos elemntos tiene uns lista
print(len(lista))

#comoa gregar un elelmto a una lista
lista.append("termineitor")
print(lista)

#como ingresar un elemto en un lugar especifico
lista.insert(0, "owo")#el primero = indice, segundo = objeto a insertar
print(lista)

##como elimnar un elelmto de una lista
lista.remove("owo")#en los conchetes se indica que elemto se eliminara
print(lista)

#eliminar el ultimo elemtos
lista.pop()
print(lista)

#eliminar un indice espesifico
del lista[0]
print(lista)

