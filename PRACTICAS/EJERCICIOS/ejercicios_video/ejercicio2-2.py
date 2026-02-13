# Creamos una función que determina si un número es primo
def numeros_primos_range(num):
    # Recorremos los números desde 2 hasta (num - 1)
    # para verificar si existe algún divisor distinto de 1 y del propio número
    for numero in range(2, num - 1):
        # Si el residuo de la división es 0, significa que el número
        # es divisible por otro valor diferente de 1 y de sí mismo,
        # por lo tanto, no es un número primo
        if num % numero == 0:
            return False

    # Si no se encontró ningún divisor, el número es primo
    return True


# Creamos una función que genera una lista de números primos
def ingreso_numero(num):
    # Inicializamos una lista vacía donde se almacenarán los números primos
    primos = []

    # Recorremos los valores desde 3 hasta el número ingresado (inclusive)
    for i in range(2, num + 1):
        # Llamamos a la función numeros_primos_range para verificar
        # si el número actual es primo
        resultado = numeros_primos_range(i)

        # Si la función retorna True, el número es primo
        # y se agrega a la lista
        if resultado == True:
            primos.append(i)

    # Retornamos la lista de números primos obtenidos
    return primos


# Llamamos a la función ingreso_numero con el valor 17
resultado = ingreso_numero(17)

# Imprimimos la lista resultante
print(resultado)

#Primos pero con lambda
#Lo mismo pero con lambda
primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num+1)))

print(primos_hasta(17))




  