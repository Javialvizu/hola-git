#Creamos las viariables a utilizar en el programa
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
mensaje = f"Hola soy {nombre} y estudio Ingenieria"

#Impresion con f-string
print(f"Hola me llamo {nombre} y tengo {edad} años")

#Creacion de una lista
datos = ["Javier",21,True]
print(datos)

#Modificacion de la lista
datos[0]= "Madeline"
print(datos)

#Creacion de una tupla(NO se puede modificar)
tupla = ("Javier","Ingeniero",21)
print(tupla)

#Creacion de un conjunto
conjunto = {"Javier",21,"Javier"}
print(conjunto)#Un conjunto no tiene un orden y si solo imprime 1 vez datos duplicados

#Creaccion de un diccionario
diccionario = {
    "nombre":"Javier",
    "edad":21,
    "profesion":"Ingeniero"
}
print(diccionario)

#Modificacion de un diccionario
diccionario["nombre"] = "Madeline"
print(diccionario)

#Uso de funciones "in" y "not in"
print("Hola" in mensaje)
print("Javier" in mensaje)
print("Javier" not in mensaje)


