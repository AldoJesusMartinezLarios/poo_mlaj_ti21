"""
    Reto 1
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 03/02/2023
    Descripción: Programa que calcula el promedio de calificaciones 
"""

matricula = int(input("Matricula: "))

calificacion1 = float(input("Calificacion 1: "))
calificacion2 = float(input("Calificacion 2: "))
calificacion3 = float(input("Calificacion 3: "))
calificacion4 = float(input("Calificacion 4: "))
calificacion5 = float(input("Calificacion 5: "))

promedio = (calificacion1+calificacion2+calificacion3+calificacion4+calificacion5)/5

print("Matricula: ", matricula)
print("Promedio: ", promedio)
