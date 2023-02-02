"""
    Programa 8
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 02/02/2023
    Descripción: Compara dos números e imprime el mayor de ellos
"""

"""
    1.- Operadores Aritmeticos
    + - / * // % **

    2.- Operadores de asignación
    =, +=, -=, /=, *=, //=, %=, **=

    3.- Operadores lógicos
    and, or, not

    5.- Operadores de membrecia (membership)
    in not in

    if condicion:
        codigo

    if condicion:
        codigo
    else:
        codigo

    if condicion:
        codigo
    elif condicion:
        codigo
    else:
        codigo
"""

numero1 = int(input("Escribe un número: ")) #Pide un valor al usuario
numero2 = int(input("Escriba otro número: ")) #Pide otro valor al usuario

if numero1 == numero2: #Condicion
    print("None") #Imprime un mensaje
elif numero1 < numero2: #Condicion
    print("Mayor: ",numero2) #Imprime un mensaje
elif numero2 < numero1: #Condicion
    print("Mayor: ",numero1) #Imprime un mensaje
