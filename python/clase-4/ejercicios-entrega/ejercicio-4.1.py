#ejercicio 1 eliminar doplicados de una lista
#escriba un programa donde tenga una lista y acontinuacion elimine los elemtos repetidos
#por ultimo mmnostrar la lista

#se crea una lista y otra como nueva lista basia
lista = ["perro", "perro", 2, 4]
newlis = []

#se recorre cada elemto de la lista
for i in range(len(lista)-1):

    #se comprueba si el primeer elemnto de la lista es diferen al segundo elemto
    if lista[i] != lista[i+1]:

        #si es verdadero entonces se agregra ese primer elemto ala nueva lista
        newlis.append(lista[i])

#se imprime la nueva lista
print(newlis)


#recien vi el video y pude averlo hecho con set nomas :,v