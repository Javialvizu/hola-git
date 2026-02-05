#Variables duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_actual = 1.5

#Variables de crudos
curso_promedio = 5
curso_actual_crudo = 3.5

"--- A. Analisis de duracion de cursos ---"
#Diferencias de duaracion entre cursos(calculo de tiempo vacio)
diferencia_curso_min = 100 - curso_actual / otros_cursos_min * 100
print(diferencia_curso_min, "%")

diferencia_curso_max = 100 - curso_actual / otros_cursos_max * 100 #Podemos modificar los 0 para combenencia de lso decimales....
resultado = round(diferencia_curso_max,2)
print( resultado, "%")  

diferencia_curso_promedio = 100 - curso_actual / otros_cursos_promedio * 100
print(diferencia_curso_promedio, "%")           

"--- B. Analisis de promedio de cursos ---"
promedio_cursos_crudos = 100 - otros_cursos_promedio * 1000 // curso_promedio / 10
print("El promedio de mis cursos crudos es: ", promedio_cursos_crudos, "%")

promedio_curso_actual = 100 - curso_actual * 1000 // curso_actual_crudo / 10
print("El promedio de mi curso actual crudo es: ", promedio_curso_actual, "%")


