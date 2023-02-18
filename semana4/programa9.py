"""
    Programa 9
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 09/02/2023
    Descripción: Compara dos números e imprime el mayor de ellos
"""

def mayor (numero1, numero2): #define la función mayor con dos variables
    result = None # Creacion de la variable result
    if numero1 > numero2: #Condicion si numero1 es mayor que numero2
        result = numero1 #Asigna el valor de la variable numero1 a la variable result
    elif numero2 > numero1: #Condicion si numero2 es mayor que numero1
        result = numero2 #Asigna el valor de la variable numero2 a la variable result
    return result #Regresa el valor result

print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #None
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #None
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1