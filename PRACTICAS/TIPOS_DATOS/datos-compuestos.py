"---Listas sinples en python---"
list = ["Javier Alvizures", "Soy ingeniero", 25, True, "Javier Alvizures"]
print(list)
list[0] = "Madeline Alvizures" #Modificamos el primer elemento de la lista
print(list[0])

"---Lista tipo tupla---"
tupla = ("Javier Alvizures", "Soy ingeniero", 25, True, "Javier Alvizures")
#tupla[0] = "Madeline Alvizures" #No se puede modificar una tupla
print(tupla[0])

"---Creando un conjunto set---"
conjunto = {"Javier Alvizures", "Soy ingeniero", 25, True, "Javier Alvizures"}
print(conjunto)#El conjunto elimina los datos repetidos
#conjunto[1] = "Madeline Alvizures" #No se puede modificar un conjunto(Los datos estan desordenados)
#print(conjunto[1]) #No se puede acceder a un conjunto por indice
conjunto = {"JAjajajaja maquina te jodi"}#Modificamos el conjunto
print(conjunto)

"---Diccionario en python---"
diccionario = {
    "nombre": "Javier Alvizures",
    "profesion": "Ingeniero",
    "edad": 25,
    "soltero": False      
}
print(diccionario["nombre"]) #Accedemos al valor de la clave "nombre"
diccionario["nombre"] = "Madeline Alvizures" #Modificamos el valor de la clave "nombre"
print(diccionario["nombre"]+ " Modificado")