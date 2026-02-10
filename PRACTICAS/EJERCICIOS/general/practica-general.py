"""def registrar_estudiante():
    condicional = "0"
    lista_estudiantes = []
    while condicional != "salir":
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = input("Ingrese su edad: ")
        carrera = input("Ingrese su carrera: ")
        lista_estudiantes.append((nombre,apellido,edad,carrera))
        
        condicional = input("Desea salir? ingrese (salir): ")
        condicional = condicional.lower()

    return (lista_estudiantes)

lista_estudiante = registrar_estudiante()
print(lista_estudiante)"""

def registrar_alumnos():
    condicional = "0"
    lista_alumnos = []
    while condicional != "salir":
        cadena = input("Ingrese nombre,apellido,edad,carrera: ")
        cadena = cadena.split(",")
        lista_alumnos.append(cadena)

        condicional = input("terminar (salir)" )
        condicional = condicional.lower()

    return(lista_alumnos)

alumnos = registrar_alumnos()
print(alumnos)
