es_igual_que = 5 == 6
es_distitno_de = 5 != 6
es_mayor_que = 5 > 6
es_menor_que = 5 < 6
es_mayor_o_igual_que = 5 >= 6
es_menor_o_igual_que = 5 <= 6   

print("5 es igual que 6:", es_igual_que)
print("5 es distinto de 6:", es_distitno_de)
print("5 es mayor que 6:", es_mayor_que)
print("5 es menor que 6:", es_menor_que)
print("5 es mayor o igual que 6:", es_mayor_o_igual_que)
print("5 es menor o igual que 6:", es_menor_o_igual_que)
#Devolucion de tipos de datos
dato = type(es_igual_que)
print("El tipo de dato de la variable es:", dato)

"---Comparacion de varias variables---"
a = 10
b = 3
c = 8

comparacion = b + c > a
print("El resultado de la comparacion es:", comparacion)

"---Comparacion de cadenas de texto---"
contraseña = "admin123"
ingreso = "admin123"

print("La contraseña es correcta:", contraseña == ingreso)
