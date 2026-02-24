#Leer archivo completo
archivo = open("texto-javier.txt", encoding="utf-8")
#print(archivo.read())

#Leer solo una linea
#line_1 = archivo.readline(10) #lee la primera linea del archivo
#print(line_1)

#Leer linea por linea
linea_1 = archivo.readlines()#lee la primera linea del archivo
print(linea_1)

#Cerrar el archivo
archivo.close()