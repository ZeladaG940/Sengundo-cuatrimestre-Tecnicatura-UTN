#como definir un conjunto
set1= {"hola", 7}
set2 = set()

#repaso de conceptos
set1.add("7")
set2.add(7)
print(7 in set1)
print(set1 == set2)

#operacioens entre conjuntos
set3 = set1 | set2 #esa kinea une los dos conjuntos
print(set3)

#para saber que elemtos tiene en comun
set3 = set1 & set2
print(set3)

#asigna el valor del elemnto 1 al elemento 2
set3 = set1 - set2
print(set3)

#se marca los elemtos que no comparten
set3 = set1 ^ set2
print(set3)

#como saber si un conjunto esta en otro conjunto
print(set2.issubset(set1))

#como saber si es un super conjunto
print(set3.issuperset(set2))

#como saber si no comparten elemtos en comun
print(set3.isdisjoint(set1))

#como convertir un conjunto a inmutable
set3 = frozenset

