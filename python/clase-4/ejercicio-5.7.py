#ejercicio 8 Menu interactivo - cajero automatico
#Hacer un programam que simule un cajero automatico con un saldo inicial
#1000$ y tendra que el siguien menu de opcione.
    #ingresar dinero en al cuenta
    #retirar dinero en la cuenta
    #mostrar dinero disponble
    #salir

saldo = 1000
salir = False

#el ciclo se repetira mientras que la condicion de salir sea falsa
while salir == False:
    print()
    print("1. ingresar dinero: ")
    print("2. retirar dinero: ")
    print("3. mostrar dinero: ")
    print("4. salir")
    user = int(input("ingrese una opcion: "))

    #segun el las opciones hara algo
    if user == 1:
        aum = int(input("ingrese la cantidad de dinero: "))
        saldo += aum

    if user == 2:
        ret = int(input("ingrese la cantidad a retirar: "))
        saldo -= ret
    if user == 3:
        print( "su saldo es: " , saldo)
    if user == 4:
        salir = True


