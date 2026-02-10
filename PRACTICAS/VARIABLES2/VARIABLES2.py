#Usuario ingresa las variables
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")

#Creacion de tupla y lista
tupla = (nombre, apellido, edad)
print(tupla)
lista = {nombre, apellido, edad}
print(lista)

#DEsempaquetamiento de tupla
name, name_2, age = tupla
print(name_2)

#Creacion del diccionario
diccionario = {
    "nombre":nombre,
    "apellido":apellido,
    "edad":edad
}

print(diccionario)

#Diccionario vacio
empty_diccionary = dict.fromkeys([nombre, apellido, edad], "deconocido")
print(empty_diccionary)

#Creacion de conjunto
conjunto_1 = {"Matematicas", "Programacion", "Fisica"}
conjunto_2 = {"Programacion", "Fisica"}
conjunto_3 = {"Historio", "Arte"}

verificacion1 = conjunto_2.issubset(conjunto_1)
print(verificacion1)

verificacion2 = conjunto_3.isdisjoint(conjunto_1)
print(verificacion2)

#Diccionario + fronzet
clave = frozenset(["Javier","Alvizures"])
diccionario = {clave: "Estudiante"}

print(diccionario)