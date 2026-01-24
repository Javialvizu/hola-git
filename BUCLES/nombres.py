nombres = []

while True:
    nombre = input("Ingresa un nombre (o 'salir'): ")

    if nombre == "salir":
        break

    nombres.append(nombre)

print("\nNombres guardados:")
for n in nombres:
    print("-", n)

if not nombres:
    print("NO se ingresaron nombres")
