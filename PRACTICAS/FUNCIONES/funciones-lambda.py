numeros = [1,2,3,4,5,6,7,8,9]
#Creando funcion lambda para multiplicar num * 2
multiplicacion_por_dos = lambda X : X*2

print(multiplicacion_por_dos(5))

#Usando filter como una funcion comun
def es_par(num):
    if(num%2==0):
        return True
    
def es_impar(num):
    if(num%2!=0):
        return True

numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

numeros_impares = filter(es_impar, numeros)
print(list(numeros_impares))

#Creando lo mismo de antes pero con lambda 

numeros_pares_lambda = filter(lambda numero: numero%2 == 0, numeros)#lambda retorna
print(list(numeros_pares_lambda))