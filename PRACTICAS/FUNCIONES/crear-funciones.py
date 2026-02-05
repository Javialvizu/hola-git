#Funcion simple 
def saludar1():
    print("Hola como estas?")

saludar1()
saludar1()
saludar1()

#Funcion con parametros
name = input("Ingrese su nombre:")
sex = input("Ingrese su genero:")

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "señora"
    elif sexo == "hombre":
        adjetivo = "señor"
    else:
        adjetivo = "No existe ese genero"
    print(f"Hola {adjetivo} {nombre}, como podemos ayudarle?")

saludar(name,sex)

#Crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghijklmnopkrs"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num -2  
    c2 = num 
    c3 = num -5 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return(contraseña,num)

#Desempaquetando la funcion
password, primer_numero = crear_contraseña_random(10)

#Mostrando los resultados obtenidos 
print(f"Su contraseña nueva es: {password} y el primer numero {primer_numero}")