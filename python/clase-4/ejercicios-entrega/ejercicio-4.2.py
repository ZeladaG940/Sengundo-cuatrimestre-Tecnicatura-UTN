#ejercicio 2: operaciones de conjuntos de listas
#escriba un programam que tenga 2 listas y que haga lo siguiente
#cree la siguiente lista
    #1.lista de palabras que aprecen en las listas
    #2.lista de palabras que aparecen en la primera lista pero el la segunda no
    #3.lista de palabras que aparecen en la segunda pero en la primera no
    #4.lista de palabras que aparecen en las dos

lisa1 = [1,2,3,5,6,8,9,10]
list2 = [1,3,4,6,7,8,5,10,11]

    # 1 lista de palabras de ambas listas
conj = set(lisa1)
conj2 = set(list2)
lisPrime = conj | conj2
print(lisPrime)

    # 2 palabras que aparecen en la primera y no en la segunda
lisPrime = conj
print(lisPrime)

    # 3  palabras que aparecen en la primera y no en la segunda
lisPrime = conj2
print(lisPrime)

    # 4 lista de palabras que aparecen en las dos
print(lisPrime)