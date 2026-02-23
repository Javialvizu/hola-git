#Carptea en una misma ruta
import carpeta_modulos.saludar2 # as saludar2 (para no escribir todo eso y tener mejor un alias)
#Carpeta dentro de otra carpeta
import sys
sys.path.append("/home/javier/REPOSITORIOS/hola-git/PRACTICAS/modulo-externo") #Agregamos la ruta de busqueda de modulos
#print(sys.path) #Imprime la ruta de busqueda de modulos

import  saludar2 #Importamos el modulo saludar2 que esta dentro de la carpeta modulo-externo      

print(saludar2.saludar("Juan"))#Llamamos a la funcion saludar del modulo saludar2