#ejercicio 3: agregar personajes a uns lista
#escriba una lista donde contenga los siguientes perdonajes del señor de los anillos

#se crea una lista basia para agregar a los personajes
lista = []

#personajes
p1 = {
    "nombre": "aragon",
    "clase" : "gerrero",
    "raza"  : "dunadan del norte"
}
p2 = {
    "nombre": "galdan f",
    "clase" : "mago",
    "raza"  : "istar"
}
p3 = {
    "nombre": "legolas",
    "clase" : "arquero",
    "raza"  : "elfo sindar"
}

#se agrega cada objeto a la lista
lista.append(p1)
lista.append(p2)
lista.append(p3)
print(lista)