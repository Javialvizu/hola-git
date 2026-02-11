#Funcion donde registramos alunmos
def registrar_alumnos():
    
    lista_alumnos = []#creacion de la lista donde guardaremos los registros
    
    while True:
        cadena = input("Ingrese nombre,apellido,edad,carrera o 'salir': ")

        cadena = cadena.strip().lower()#Quitamos espacios y volvermos minusculas todo el texto

        if cadena == "salir":
            break

        datos = cadena.split(",")#separamos el texto en 4 

        if len(datos) == 4:#condicionamos que deben ver 4 elementos
            if datos[2].isnumeric():#La edad tiene que ser un numero entero

                diccionario = {#creamos un diccionario
                    "nombre": datos[0],#posicion 0 dentro de la cadena
                    "apellido": datos[1],
                    "edad": int(datos[2]),
                    "carrera": datos[3]
                }

                lista_alumnos.append(diccionario)#agregamos a la lista el diccionario

            else:
                print("Edad mal ingresada")
        else:
            print("Formato incorrecto, intente de nuevo")

    return lista_alumnos#retornamos la lista con todos los datos


alumnos = registrar_alumnos()#llamamos la funcion
print(alumnos)
#Mostrar cantidad total de alumnos
print(f"Total estudiantes: {len(alumnos)}")

#Mostrar mayores de edad
contador = 0

for mayor in alumnos:
    if mayor["edad"] >= 18:
        contador += 1

print(f"Mayores de edad: {contador}")

#Indicamos si hay ingenieros entre los alumnos 
ingenieros_bool = False

for ingenieros in alumnos:
    if ingenieros["carrera"].lower() == "ingeniero":
        ingenieros_bool = True
print(f"Hay estudiantes de ingenieria: {ingenieros_bool}")

#Imprimimos unicamente los nombres de la lista 
print("Lista de nombres:")
for nombres in alumnos:
    print(f"-{nombres["nombre"]}")

