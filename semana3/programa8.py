"""
    Programa 8
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 02/02/2023
    Descripción: Compara dos números e imprime el mayor de ellos
"""

numero1 = int(input("Escribe un número: ")) #Pide un valor al usuario
numero2 = int(input("Escriba otro número: ")) #Pide otro valor al usuario

if numero1 == numero2: #Condicion
    print(None) #Imprime una cadena
elif numero1 < numero2: #Condicion
    print(numero2) #Imprime el numero mayor en esta condicion
elif numero2 < numero1: #Condicion
    print(numero1) #Imprime el numero mayor en esta condicion
