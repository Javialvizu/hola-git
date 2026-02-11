#Version optima
"""def registrar_estudiante():
    condicional = "0"
    lista_estudiantes = []
    while condicional != "salir":
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        carrera = input("Ingrese su carrera: ")
        lista_estudiantes.append((nombre,apellido,edad,carrera))
        
        condicional = input("Desea salir? ingrese (salir): ")
        condicional = condicional.lower()

    return (lista_estudiantes)

lista_estudiante = registrar_estudiante()
print(lista_estudiante)"""


def registrar_alumnos():
    lista_alumnos = []

    while True:
        cadena = input("Ingrese nombre,apellido,edad,carrera o 'salir': ")

        cadena = cadena.strip().lower()

        if cadena == "salir":
            break

        datos = cadena.split(",")

        if len(datos) == 4:
            if datos[2].isnumeric():

                diccionario = {
                    "nombre": datos[0],
                    "apellido": datos[1],
                    "edad": int(datos[2]),
                    "carrera": datos[3]
                }

                lista_alumnos.append(diccionario)

            else:
                print("Edad mal ingresada")
        else:
            print("Formato incorrecto, intente de nuevo")

    return lista_alumnos


alumnos = registrar_alumnos()
print(alumnos)
#Mostrar cantidad total de alumnos
print(f"Total estudiantes: {len(alumnos)}")

#Mostrar mayores de edad
contador = 0

for mayor in alumnos:
    if mayor["edad"] >= 18:
        contador += 1

print(f"Mayores de edad: {contador}")

ingenieros_bool = False

for ingenieros in alumnos:
    if ingenieros["carrera"].lower() == "ingeniero":
        ingenieros_bool = True
print(f"Hay estudiantes de ingenieria: {ingenieros_bool}")

print("Lista de nombres:")
for nombres in alumnos:
    print(f"-{nombres["nombre"]}")

