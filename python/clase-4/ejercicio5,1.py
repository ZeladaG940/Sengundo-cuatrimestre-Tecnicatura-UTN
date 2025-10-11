#aser un rango de numro que sume numeros pares
pares = 0
for i in range(0,10,1):
    if i % 2 == 0:
        pares += i

print(pares)