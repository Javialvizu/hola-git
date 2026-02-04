#Creando conjunto con set()
conjunto = set(["Javier",("Alvizures",21)])#Solo las tuplas pueden ir dentro de un conjunto
print(conjunto)

#Creando conjunto con llaves {}
conjunto = {"Javier",("Alvizures",21)}
print(conjunto)

#Meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Javier","Alvizures"])
conjunto2 = {conjunto1, 21}
print(conjunto2)

#Teoria de conjuntos
conjunto_a = {1,2,3,4,5,6,7,8}
conjunto_b = {4,5,6}
conjunto_c = {6,7,8,9,10}

#Versificar si un elemento esta en un conjunto .issubset/<=
resultado = conjunto_b.issubset(conjunto_a) #Revisa si el conjunto_b es subconjunto del conjunto_a
print(resultado)

resultado = conjunto_a <= (conjunto_c) #Revisa si el conjunto_c es superconjunto del conjunto_a
print(resultado)

#Verificar si es un superconjunto .issuperset/>=
resultado = conjunto_a.issuperset(conjunto_b) #Revisa si el conjunto_a
print(resultado)
resultado = conjunto_c >= (conjunto_a) #Revisa si el conjunto_c es superconjunto del conjunto_a
print(resultado)

#Verificar si hay un numero en comun 
resultado = conjunto_a.isdisjoint(conjunto_c) #Revisa si no hay numeros en comun entre los dos conjuntos
print(resultado)
