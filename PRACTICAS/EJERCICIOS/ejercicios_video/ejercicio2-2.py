def numeros_primos_range(num):
    for numero in range(2,num-1):
        if num % numero == 0: return False
    return True

def ingreso_numero(num):
    primos = []
    for i in range(3,num+1):
        resultado = numeros_primos_range(i)
        if resultado == True:
            primos.append(i)
    return primos

resultado = ingreso_numero(17)
print(resultado)   