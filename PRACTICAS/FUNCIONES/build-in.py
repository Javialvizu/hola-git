numeros = [4,8,3]

#Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#Redondiando a 6 decimales
numero = round(12.123455,2)
print(numero)

#Retorna False -> 0, vacio, False, none \ True -> distitnto a 0, True, cadena, datos no vacios
resultado_bool = bool()
print(resultado_bool)

#Retorna True si todos los valores son verdaderos 
resultado_all = all([234,"True",0])#Aqui comprueba que todos los valores de la lista sean true
print(resultado_all)

#Suma todos los valores de un iterable 

suma_total = sum(numeros)
print(suma_total)
