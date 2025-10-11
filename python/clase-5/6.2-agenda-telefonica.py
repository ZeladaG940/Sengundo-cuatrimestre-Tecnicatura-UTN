#ejercicio 11: Agenda telefonica
#Hacer un programa que simule una agenda de contactos. Crear un diccioario
#donde la clasve sea el nombre del usuario y el valor sea el telefono, el programa,
#tendra el siguiente menu de opciones
    #1. nuevo contacto
    #2. borrar contacto
    #3. ver contacto
    #4. salir


#cree el objeto
user = {
    "keys": "user",
    "tele": " "
}

#menu
print("1. nuevo contacto")
print("2. borrar contacto")
print("3. ver contacto")
print("4. salir")

#si dalir es falso el ciclo seguira
salir = False
while salir == False:

    #comprobaciones
    menu = int(input("Ingresa una opcion: "))
    if menu == 1:
        user["tele"] = int(input("Ingresa el telefono: "))
    if menu == 2:
        user["tele"] == " "
        print("sin contactos..")
    if menu == 3:
        print(user["tele"])

    #4 = al cambio de valor de salir a verdadero
    if menu == 4:
        salir = True
