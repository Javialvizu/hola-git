lista_alumnos = []

def registros_alumnos():
    cadena = input("Ingrese: nombre,apellido,edad,carrera: ")
    datos = cadena.split(",")
    
    if len(datos) == 4 and datos[2].isnumeric():
        alumno = {
            "nombre":datos[0],
            "apellido":datos[1],
            "edad":int(datos[2]),
            "carrera":datos[3]
        }
        lista_alumnos.append(alumno)
        
        print(f"Alumno {alumno["nombre"]} registrado")
        
    else:
        print("Datos invalidos")

def mostrar_alumnos():
    for alumnos in lista_alumnos:
        print(f"-{alumnos['nombre'].capitalize()} {alumnos['apellido'].capitalize()} {alumnos['edad']} {alumnos['carrera'].capitalize()}")

def contar_mayores():
    contador_mayor = 0
    contador_menor = 0
    for mayor in lista_alumnos:
        if mayor['edad'] >= 18:
            contador_mayor +=1
        else:
            contador_menor += 1
    print(f"Mayores de edad: {contador_mayor}")
    print(f"Menores de edad: {contador_menor}")

def buscar_por_nombre():
    nom = input("Ingrese el nombre que desea buscar: ")
    for nombre in lista_alumnos:
        if nombre['nombre'] == nom:
            print(f"-{nombre['nombre'].capitalize()} {nombre['apellido'].capitalize()} {nombre['edad']} {nombre['carrera'].capitalize()}")

def hay_ingenieros():
    contador_ingenierios = False
    for inge in lista_alumnos:
        if inge['carrera'].lower() == "ingeniero":
            contador_ingenierios = True
    print(f"Existen alumnos ingenieros? {contador_ingenierios}")


def menu():
    while True:
        print("-----MENUS DE OPCIONES-----")
        print("1-Ingresar alumno")
        print("2-Mostrar alumnos")
        print("3-Contar mayores de edad")
        print("4-Buscar alumno por nombre")
        print("5-Ver si hay ingenieros")
        print("6-Salir")
    
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            registros_alumnos()
        elif opcion == 2:
            mostrar_alumnos()
        elif opcion == 3:
            contar_mayores()
        elif opcion == 4:
            buscar_por_nombre()
        elif opcion == 5:
            hay_ingenieros()
        elif opcion == 6:
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida!!!")


menu()
        
            

