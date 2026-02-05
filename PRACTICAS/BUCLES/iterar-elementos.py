#Creamos la lista(Funciona exactamente igual para tuplas y conjuntos)
animales = {"perro","gato","loro","cocodrilo"}
numeros = {0,1,2,3,4,5,6,7,8,9,}


#PAsa por toda la lsita "animal" se vuelve en cada vuelta cada uno de los elementos
for animal in animales:
    print(f"La variable animal ahora mismos es: {animal}")

print("-------------------------------------------------")

for numero in numeros:
    resultado = numero * numero
    print(f"{numero} al cuadrado es igual a {resultado} ")

#for con 2 listas interadas
for numero, animal in zip(numeros,animales):
    print(f"Recorriendo lista numeros: {numero}")
    print(f"Recorrinedo lista animales: {animal}")

print("---------------------------------------------------------")

#Iterando con funcion range
for num in range(5,10):
    print(num)

print("------------------------------------------------------")

#Funcion enumerate
for animal in enumerate(animales):
    indice = animal[0]#0 significa indice 
    valor = animal[1]#1 significa valor
    print(f"El indice  es: {indice} y el valor es {valor}")

print("-------------------------------------------------------------")
#BUcle for + else
for numero in numeros:
    print(f"La lista contiene los numeros: {numero}")
else:
    print("La lista finalizo")