frutas = ["Manzana","Banana","Fresa","Melocoton","Sandia"]
cadena = "Hola Javier"
numeros = [0,1,2,3,4,5,6,7,8,9]

#Evitando que se coma una banana con la funcion continue
for fruta in frutas:
    if fruta == "Banana":
     continue
    print(f"La fruta es: {fruta}")

#Evitar que el bucle siga ejecutandose cuando llegue a 
for fruta in frutas:
   if fruta == "Fresa":
        break  
   print(f"Me voy a comer una: {fruta}")#POdemos primero imprimir para que si se coma la fresa...

print("Bucle terminado")

#Recorrer una cadena de texto
for letra in cadena:
   print(letra)

#For en una sola linea de codigo
numeros_duplicados = list()
for num in numeros:
   numeros_duplicados.append(num*num)
else:
   print(numeros_duplicados)




 