with open("texto-javier.txt", "w", encoding="utf-8") as archivo:
#Sobreiscribiendo el archivo, si el archivo no existe lo crea
   # archivo.write("Hola, este es un texto de prueba ")
#Writelines acumula los textos en una lista y los escribe en el archivo, es necesario agregar el salto de linea \n para que cada texto se escriba en una nueva linea
    archivo.writelines(["Hola como estas?\n","Escribir en archivos"])
    archivo.writelines(["\n","Otra linea mas"])
   