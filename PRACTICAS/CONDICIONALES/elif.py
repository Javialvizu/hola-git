ingreso_mensual = int(input("Ingrese su sueldo mensual:"))
gasto_mensual = int(input("Ingrese su gasto mensual:"))

if ingreso_mensual >= 10000:
    print("Tienes un buen sueldo")
    if ingreso_mensual - gasto_mensual > 3000:
        print("Ademas eres ahorrativo")
    elif ingreso_mensual -gasto_mensual <= 0:
        print("Valiste ya te jodiste xd")
    else:
        print("Deberias controlar tus gastos")

elif ingreso_mensual > 5000:
    print("Tienes un sueldo justo para latinoamerica")

elif ingreso_mensual > 2000:
    print("Tienes un sueldo bajo")

elif ingreso_mensual > 500:
    print("Venezuela es tu hogar :(")

else:
    print("Eres un tremendo pobre xd :(")