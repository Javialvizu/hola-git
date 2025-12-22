print("-----CALCULADORA BASICA-----")

num1 = float(input("Ingrese numero:"))
num2 = float(input("Ingrese numero:"))


print("-----OPCIONES-----")
print("1.SUMA ")
print("2.RESTA ")
print("3.MULTIPLICACION")
print("4.POTENCIA ")
print("5.DIVISION ")
print("6.DIVISION ENTERA ")
print("7.RESIDUO DIVISION ")
print("-------------------")

op = input("Elije una opcion: ")

if op == "1":
    print(num1 + num2)
elif op == "2":
    print(num1 - num2)
elif op == "3":
    print(num1  * num2)
elif op == "4":
    print(num1  ** num2)
elif op == "5":
    print(num1  / num2)
elif op == "6":
    print(num1  // num2)
elif op == "7":
    print(num1  % num2)
else:
    print("Opcion inexistente!!!")
