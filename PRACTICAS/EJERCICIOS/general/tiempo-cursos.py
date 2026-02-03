curso_normal = 6 #horas 70%
curso_rapido = 3.5 #horas 30%

curso_normal_crudo = 8 #horas
curso_rapido_crudo = 4 #

"---PARTE A: Comparacion de duracion de cursos---"
print(f"El curso rapido dura {100 - (curso_rapido / curso_normal * 100):.2f}% menos que el normal")
print(f"El curso normal dura {(curso_normal / curso_rapido * 100) - 100:.2f}% mas que el rapido")


"---PARTE B: Comparacion de duracion cruda de cursos---"
print(f"Existe un {100 - (curso_rapido_crudo / curso_normal_crudo * 100):.2f} % de conenido inutil")
print(f"El curso rapido tiene un { (curso_normal_crudo / curso_rapido_crudo * 100)-100:.2f} % de contenido real ")