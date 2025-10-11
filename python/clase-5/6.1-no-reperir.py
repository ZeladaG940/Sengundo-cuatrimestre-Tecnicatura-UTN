#ejercicio 10: No repetir caracteres
#aser un programam que pida una cadena de caracteres
#luego meterlo en una lista sin repetir caracteres

#se guarda la frase en una variable
texto = str(input("ingrese la frace: "))

#se ccrea uma lista que va a guardar cada letra mas adelante
lista = []

#iteramos
for i in texto:

    #si no esta en la lista se agregara ala lista(si existe una letra que esta en la lista no se agregara)
    if i not in lista:
        lista.append(i)

print(lista)