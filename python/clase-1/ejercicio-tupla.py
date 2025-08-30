#dada la siguiente tupla
tupla = (13,1,8,3,2,5,5)
#crea una lista que solo incluya los numeros menmores a 5
lista = []
for i in tupla:
     if i < 5:
         lista.append(i)

print(lista)