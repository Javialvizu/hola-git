#Creacion de diccionaro con dict()
diccionario = dict(nombre="Javier", apellido="Alvizures", edad=21)
print(diccionario)

#Crear diccionario con fronmkeys()
diccionario = dict.fromkeys(["nombre","apellido"])
print(diccionario)

diccionario = dict.fromkeys("ABCDE")#Esto es un iterable por eso es necsario hacer una lista []
print(diccionario)

#CAmbianod valor por defecto por no se 
diccionario = dict.fromkeys(["nombre","apellido"],"no se")
print(diccionario)

#Las listas no pueden ser claves las tuplas si(no pueden ser mutables) o set
diccionario = {("Javier","Alvizures"):"Nombre"}
print(diccionario)

diccionario = {frozenset(["Javier","Alvizures"]):"Nombre"}
print(diccionario)