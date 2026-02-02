cadena1 = "hola,soy,Javier,Alvizures"
cadena2 = "estoy aprendiendo Python  "

"Metodos para cadenas de texto"
#Convierte a mayusculas
resultado = cadena1.upper()
print(resultado)

resultado = "Hola crack".upper()
print(resultado)

#Convierte a minusculas
resultado = cadena2.lower()
print(resultado)   

#Primera letra en mayuscula
resultado = cadena1.capitalize()
print(resultado)

"Metoso buscan un valor"
#Buscamos una cadena en otra cadena
resultado = cadena1.find("soy")#Nos devuelve la posicion donde se encuentra en caso no exitir nos devuelve -1
print(resultado)

#Busqueda de cadena en otra cadena(NO DEVUELVE ERROR EN CASO DE NO EXISTIR)
resultado = cadena1 .index("a")
print(resultado)

"Consultan datos embace a type"
#Cosultar si es numeroico, devolver true o false
resultado = cadena1.isnumeric()
print(resultado)

#Consultar si es alfabetico, devolver true o false
resultado = cadena1.isalpha()
print(resultado)

"Contadores de datos"
#Contar cuantas veces aparece un caracter en una cadena
resultado = cadena1.count("a")
print(resultado)

#Contar cuantos caracteres tiene una cadena
resultado = len(cadena1)
print(resultado)

#Verificar si una cadena empieza con otra cadena
resultado = cadena1.startswith("hola")
print(resultado)

#Verificar si una cadena termina con otra cadena
resultado = cadena1.endswith("Javier")
print(resultado)

#Remplazar valor en una cadena
resultado = cadena1.replace(",", " ")   
resultado = resultado.capitalize()
print(resultado)

#Dividir una cadena en varias partes
resultado = cadena1.split(",")
print(resultado)
print(resultado[2])
#Eliminar espacios en blanco al inicio y al final de una cadena
resultado = cadena1.strip()
print(resultado)






