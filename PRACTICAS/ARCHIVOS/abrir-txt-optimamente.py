#Abriendo el archivo con with open
with open("texto-javier.txt", encoding = "UTF-8") as archivo:
    print(archivo.read())

#No es necesario cerrarlo al utilizar with open 