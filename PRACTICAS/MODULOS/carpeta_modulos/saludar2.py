#Llamamos al módulo_saludar, que se encuentra en el mismo directorio que este archivo
import modulo_saludar as m_saludar

#Llamamos a la función saludar del módulo_saludar, pero con el alias m_saludar
from modulo_saludar import saludar, saludar_raro

print(m_saludar.saludar("Javier"))
print(type(m_saludar))

print(saludar("Alvizures"))
print(saludar_raro("Javier"))

print(dir(m_saludar))