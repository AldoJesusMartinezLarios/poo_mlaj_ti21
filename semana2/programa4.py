"""
    Programa 4
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 26/01/2023
    Descripción: Suma de dos numeros utilizando .format
"""

numero1 = 10 #primera variable
numero2 = 5 #segunda variable

print("{}+{}={}".format(numero1,  numero2, numero1+numero2)) #sentencia que imprime 10+5=15

print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2)) #utilizacion por nombre

print("{n2}+{n2}={n2}".format(n1=numero1,n2=numero2,suma=numero1+numero2)) #imprime

print("{numero1}+{numero2}={suma}".format(numero1=numero1,numero2=numero2,suma=numero1+numero2)) #imprime

print("{numero1}+{numero2}".format(numero1,  numero2, numero1+numero2)) #error por que no asigna variable
