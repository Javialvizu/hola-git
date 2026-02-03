diccionario = {
    "nombre": "Javier", 
    "apellido": "Alvizures",    
    "edad": 21,
    "ciudad": "Guatemala"
}

print(diccionario)


# Obtener todas las claves del diccionario
claves = diccionario.keys()
print(claves)

#Obtener valores por id de diccionario
claves = diccionario.get("nombre")#Si no existe la clave devuelve None
print(claves)

#Eliminar un elemnto del diccionario
eliminar = diccionario.pop("nombre")
print(diccionario)

#ONbteniendo un iterable de valores
valores_iterables = diccionario.items()
print(valores_iterables)    

#Elimina todos los valores del diccionario
diccionario.clear()
print(diccionario)

