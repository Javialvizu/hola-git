frase = input("Ingrese una frase con formato nombre,apellido,edad,ciudad: ")
print(frase)

# ---------- PARTE 1 (métodos de string) ----------
frase = frase.strip()
print(frase)

frase = frase.lower()
print(frase)

frase = frase.replace(",", " ")
print(frase)

frase = frase.capitalize()
print(frase)

lista_datos = frase.split(" ")
print(lista_datos)

# ---------- PARTE 2 (listas) ----------
cantidad_elementos = len(lista_datos)
print("Cantidad de elementos:", cantidad_elementos)

lista_datos.insert(1, "python")
print(lista_datos)

lista_datos.pop(-1)
print(lista_datos)

print("python" in lista_datos)

# ---------- PARTE 3 (diccionario) ----------
diccionario = {
    "nombre": lista_datos[0],
    "apellido": lista_datos[1],
    "edad": lista_datos[2],
    "ciudad": lista_datos[3]
}

print(diccionario)

print(diccionario.get("nombre"))

diccionario.pop("edad")
print(diccionario)

print(diccionario.keys())
print(diccionario.items())
