#recorremos el diccionario de la selelcio Aegentina
seleccionArgentina = {
    10: {
        "nombre": "Lionel",
        "apellido": "Messi",
        "edad": 38,
        "altura": 1.70,
        "posicion": "Delantero"
    },
    1: {
        "nombre": "Emiliano",
        "apellido": "Martínez",
        "edad": 33,
        "altura": 1.95,
        "posicion": "Arquero"
    },
    6: {
        "nombre": "Cristian",
        "apellido": "Romero",
        "edad": 27,
        "altura": 1.85,
        "posicion": "Defensor"
    },
    7: {
        "nombre": "Ángel",
        "apellido": "Di María",
        "edad": 37,
        "altura": 1.80,
        "posicion": "Mediocampista"
    }
}

#con el metodo de items sew recorre el diccionario
for i in seleccionArgentina.items():
    print(i)