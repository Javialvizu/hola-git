#Forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero

    return numeros_sumados

resultado = suma([2,4,6,50])
print(resultado)

#Forma optima de hacerlo (args)
def suma(*numeros):
    return sum(numeros)

resultado = suma(4,4,8,2,2)
print(resultado)
