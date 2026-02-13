#Creando funcion que muestre la serie fibonacci entre 0 y el numero dado    
def fibonnaci(num):
    a,b = 0,1
    fibonnaci_lista = [0]
    for i  in range(num):
        if b > num: return fibonnaci_lista
        else:
            fibonnaci_lista.append(b)
            a , b = b , a + b
        
        

lista = fibonnaci(20)
print(lista)

