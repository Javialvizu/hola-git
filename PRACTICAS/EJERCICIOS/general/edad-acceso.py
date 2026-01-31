
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))  

if edad >= 18:
    print(f"Hola {nombre}, eres mayor de edad y puedes acceder al sitio.")

elif edad >= 12:
    print(f"Hola {nombre}, eres menor de edad y no puedes acceder al sitio.")
else:
    print(f"Hola {nombre}, eres un niño y no puedes acceder al sitio.") 