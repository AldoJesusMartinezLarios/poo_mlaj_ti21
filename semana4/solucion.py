"""
    Programa 8
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 07/02/2023
    Descripción: Compara dos números e imprime el mayor de ellos
"""

n1 = int (input("Número 1: "))
n2 = int (input("Número 2: "))

# Solucion 1
if n1 > n2:
    print(n1)
if n2 > n1:
    print(n2)
if n1==n2:
    print (None)

#Solucion 2
if n2 > n1:
    print(n2)
if n1 > n2:
    print(n1)
else :
    print (None)

#Solucion 3
if n2 < n1:
    print(n1)
elif n1 < n2:
    print(n2)
else:
    print (None)

#Solucion 4
if n1 == n2:
    print(None)
elif n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)

#Solucion 5
if n1<n2:
    print(n2)
if n2 < n1:
    print(n1)
if n1==n2:
    print(None)

#Solucion 6
if n1>n2:
    print(n1)
if n2>n1:
    print(n2)
else:
    print(None)

#Solucion 7
if (n2<n1 or n1>n2):
    print(n1)
elif (n1<n2 or n2>n1):
    print(n2)
else:
    print (None)

#Solucion 8
if n1<=n2:
    if n2 == n1:
        print(None)
    else:
        print(n2)
else:
    print(n1)

#Solucion 9
if n1 > n2:
    print(n1)
elif n2 >= n1:
    if n2 == n1:
        print(None)
else:
    print(n2)

#Solucion 10
if n1==n2:
    print (None)
elif n1 < n2:
    print(n2)
else:
    print(n1)
    
#Solucion 11
if n1 <= n2 and n2==n1:
    print (None)
elif n1 < n2:
    print (n2)
else:
    print (n1)
