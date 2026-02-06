#Pedir el nombre y la edad de los compañeros que ingresaron hoy a la clase

#Funcion para obtener el profesor y el asistente segun la edad
def obtener_compañeros(cantidad_de_compañeros):

    #Creando lista vacia donde se guardaran los compañeros
    compañeros = []

    #For para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre:")
        edad = int(input("Ingrese la su edad:"))
        compañero = (nombre,edad)#Creamos un tupla

        #Agregamos informacion a la lista
        compañeros.append(compañero)

    #Ordenamos con sort de menor a mayor segun su edad 
    compañeros.sort(key=lambda x:x[1])

    #Compañeros[x] devuelve un tupla con (nombre,edad) accedemos a nombre con 0 y al edad con 1
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    #Retornamos una tupla
    return compañeros,asistente,profesor

#Desempaquetamos lo que nos retorna la funcion
compañeros,asistente,profesor = obtener_compañeros(3)
print("------La lista de estudiantes------")
print(compañeros)
print("----------------------------------------------")
print(f"El profesor es: {profesor} y el assistente es: {asistente}")

