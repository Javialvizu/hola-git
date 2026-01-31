numero = int(input("INgrese un numero:"))

if numero % 3 == 0 and numero % 5 == 0:
    print("Numero es multiplo de 3 y 5")
elif numero % 3 == 0:
    print("Numero es multiplo de 3")
elif numero % 5 == 0:
    print("Numero es multiplo de 5")

else:
    print("Numero no es mutilo de 3 ni de 5")
    
    
         