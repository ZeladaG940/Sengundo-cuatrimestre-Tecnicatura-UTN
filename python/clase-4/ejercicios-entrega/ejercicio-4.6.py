#ejercicio 1:
#llenar una lista con numeros del 1 al  50, luego mostrar la lista
#los elemtos deben mostrarse de menor a mayor

lista = []
i = 1;
while i<50:
    lista.append(i)
    i += 1
for i in lista:
    print(i, end="-")# end agrega un - a cada iteracion