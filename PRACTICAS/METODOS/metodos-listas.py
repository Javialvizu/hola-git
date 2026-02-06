#Creacion de una lista
lista = list(["Javier","Alvizures",True,False,True,False,False])
print(lista)
lista_numeros = [2,3,5,121,61,8,9]

#Devuelve la longitud de la lista
cadena = "Hola"
resultado = len(lista)
print(resultado)    

#Agregando elementos a la lista
agregar = lista.append("Guatemala")
print(lista)

#Agregar un elemento en una posicion especifica
agregar_specifica = lista.insert(1, "Crack")
print(lista)

#Agregar varios elementos a la lista
lista.extend(["Python","Django","Flask"])
print(lista)

#Eliminar un elemento en una posicion especifica
eliminar_posicion = lista.pop(0)
print(lista)

#Eliminar el ultimo elemento de la lista
eliminar_ultimo = lista.pop(-1)
print(lista)

#Eliminar un elemento de la lista
lista.remove("Crack")
lista.remove("Alvizures")
lista.remove("Guatemala")
lista.remove("Django")
lista.remove("Python")

print(lista)

#Ordenar la lista(Del menor al mayor)
lista_numeros.sort()
print(lista_numeros)

#Ordenar la lista(Del mayor al menor)   
lista_numeros.sort(reverse=True)
print(lista_numeros)

#Invertir el orden de la lista
lista.reverse()
print(lista)    

#Verificanod si un elemento existe en la lista
existe = lista.index(False)#Devuelve la posicion del elemento (solo busca elementos completos)
print(existe)


#Eliminar todos los elementos de la lista
lista.clear()
print(lista)
