usuario =  {
    "nombre":"Javier",
    "apellido":"Alvizures",
    "edad":21
}

#Recorriendo diccionario para mostrar la clave
for key in usuario:
    print(key)

#Recorriendo diccionario para mostrar clave y variables con .item()
for datos in usuario.items():
    key = datos[0]
    variables = datos[1]
    print(f"La clave es: {key} - El valor es: {variables}")