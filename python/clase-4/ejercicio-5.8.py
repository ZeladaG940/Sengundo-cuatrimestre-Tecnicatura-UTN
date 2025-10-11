#ejercicio 9
#mostrar una frace sin espacios sin espacios y encontrar su logitud
#aser un programam donde el usuario ingrese una frace, se le devolvera la misma frace pero sin espacios
#en blanco y ademas un contrador de cunatos cararacteres tiene la frace sin contar los easpcios

frace = str(input("ingrese su frace ya sea larga o corta: "))
for letra in frace:
    if letra == " ":

        #esta metodo remeplaza cada espacion en blando por un sin espacio
        newFrase = frace.replace(" ", "")

        #incio del conteo de letras
        cont = 0
        for newletras in newFrase:
            cont += 1

print(f"tienes un total de {cont} letras en la frace: {newFrase}")