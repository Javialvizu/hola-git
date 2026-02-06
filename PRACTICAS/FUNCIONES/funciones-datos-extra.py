#Maneras de definir parametros
def frase(nombre,apellido,adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

resultado = frase(apellido = "Alvizures",nombre = "Javier")
print(resultado)

#Definicion de parametrops opcionales...
def parametros(nombre, apellido, adjetivo = "tonto"): 
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

resultado1 = parametros("Javier","Alvizures", adjetivo = "Inteligente")
print(resultado1)
