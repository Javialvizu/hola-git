#Forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero

    return numeros_sumados

resultado = suma([2,4,6,50])
print(resultado)

#Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado1 = suma_total([4,4,8,2,2])
print(resultado1)

#LO mismo de arriba pero utilizando el operador * como argumento (*args) + nombre
def suma(nombre, *numeros):
    return f"{nombre}, la suma de los numeros es de: {sum(numeros)}"

resultado = suma("Javier", 8,8,8,8)
print(resultado)


