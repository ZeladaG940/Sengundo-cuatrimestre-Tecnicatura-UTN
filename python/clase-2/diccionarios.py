#diccionarios se caracterizan por tener un keys y values
diccionario = {
    "nombre": "zelada",
    "edad": "20",
    "gatos": 2
}
print(diccionario)

#como verificar la cantidad de elemtos que ahi
print(len(diccionario))

#como acceder a un elemto de un diccionario con una keys
print(diccionario["nombre"])

#como modificar elemtos con la keys
diccionario["nombre"] = "Arturo"
print(diccionario)

#como recorrer los elementos osea las keys
for i in diccionario:
    print(i)

#como reccorrer a las keys y values
for i in diccionario.items():
    print(i)

#como comprobar si existe un elemto(regresa un valor buleano
print("zelada" in diccionario)

#como modificar el value de una keys
diccionario["nombre"] = "pancho·"
print(diccionario)

#como vaciar un diccionario
diccionario.clear()
print(diccionario)#devuelve un diccionario basio

