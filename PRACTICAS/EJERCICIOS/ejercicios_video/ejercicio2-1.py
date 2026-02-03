texto = input("Ingrese un texto: ")

palabras_separadas = texto.split(" ")
cantidad_palabras = len(palabras_separadas)

print(f"Dijiste un total de {cantidad_palabras} palabras y tardarias {cantidad_palabras/2} segundos en decirlas, ")

print(f"Persona que habla rapido tardaria: {(cantidad_palabras/2)/1.5} segunods")

if cantidad_palabras > 10:
    print("Calla comunista")
else:
    print("Tremendo mudo")