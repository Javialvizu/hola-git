#Las variables se declaran y despues se definen...o modifican

print("---numeros y operaciones---")
a = 2
b = 3
c = a + b
c = a * b
print(c) #Se imprime el ultimo c que se opero (*)

"***********************************************"

print("---strings y logica de impresion ---")
nombre = ("JAVIER")
nombre = ("ROBERTO")#Se imprime la ultima definicion que se le asigno a nombre
print(nombre)

"***********************************************"

print("---Signo + y - para agregar o restar---")
a = 10
a += 1
a -= 3
print(a)

"***********************************************"

print("---Concatenacion de string----")
nombre = "Javier"
apellido = "Alvizures"
nombre1 = nombre + " " + apellido
print(nombre,apellido) #Impresion de las 2 variables
print(nombre1)#Impresion de la suma de las 2 variables

"***********************************************"

print("----f(strings)----") 
#f(string) nos funciona para convertir cualquier tipo de valor en booleano
nombre_f = True #Podemos ulilizar cualquier tipo de variable int/string/float/boolean
nombre2 = f"{nombre_f}{" "}{apellido}"
print(nombre2)

"***********************************************"

print("---Eliminar variables---")
nombre_del = True
nombre3 = f"{nombre_del}{" "}{apellido}"
del nombre_del
print(nombre3)

"***********************************************"

print("---Busacadores---")
nombre_buscador = "Javier"
bienvenida =  f"Hola como estan mis amigos soy {nombre_buscador}"
print("ola" in bienvenida)
print("pedro" in bienvenida)
print("adios" not in bienvenida)
print("Hola" not in bienvenida)
#Este lenguaje es key sensitive

#CamelCase: Utilizamos mayusculas en las iniciales
variableNueva = "CamelCase" 
#Snake: Usamos guion bajo
variable_nueva = "Snake"





