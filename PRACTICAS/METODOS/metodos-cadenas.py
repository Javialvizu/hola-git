cadena1 = "holasoyJavier"
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
#





