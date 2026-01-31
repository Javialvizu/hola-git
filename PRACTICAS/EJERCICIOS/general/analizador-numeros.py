numero = int(input("Ingrese un numero: "))  

if numero > 0:
    print(f"El numero {numero} es positivo")
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    if numero % 3 == 0:
        print(f"El numero {numero} es multiplo de 3")
    if numero > 100:
        print(f"El numero {numero} es mayor que 100")
    else:
        print(f"El numero {numero} es menor que 100")

if numero < 0:
    print(f"El numero {numero} es negativo")
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    if numero % 3 == 0:
        print(f"El numero {numero} es multiplo de 3")
    if numero > 100:
        print(f"El numero {numero} es mayor que 100")
    else:
        print(f"El numero {numero} es menor que 100")