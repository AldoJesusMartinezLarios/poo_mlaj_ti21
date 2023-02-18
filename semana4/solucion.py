"""
    Programa 8
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 07/02/2023
    Descripción: Compara dos números e imprime el mayor de ellos
"""

n1 = int (input("Número 1: ")) #Pide un numero al usuario
n2 = int (input("Número 2: ")) #Pide otro numero al usuario

# Solucion 1
if n1 > n2: #Condicion si n1 es mayor que n2
    print(n1) #Imprime n1
if n2 > n1: #Condicion si n2 es mayor que n1
    print(n2) #Imprine n2
if n1==n2: #Condicion para saber si son iguales
    print (None) #Imprime None

#Solucion 2
if n2 > n1: #Condicion si n2 es mayor que n1
    print(n2) #Imprime la variable n2
if n1 > n2: #Condicion si n1 es mayor que n2
    print(n1) #Imprime el valor de n1
else : #Si no se cumplen las condiciones anteriores se ejecuta esta
    print (None) #Imprime None

#Solucion 3
if n2 < n1: #Condicion si n2 es menor que n1
    print(n1) #Imprime n1
elif n1 < n2: #Condicion si n1 es menor que n2
    print(n2) #Imprime n2
else: #Si no se cumple lo anterior
    print (None) #Imprime None

#Solucion 4
if n1 == n2: #Condicion si n1 es igual que n2
    print(None) #Imprime None
elif n1 > n2: #Condicion si n1 es mayor que n2
    print(n1) #Imprime n1
elif n2 > n1: #Condicion si n2 es mayor que n1
    print(n2) #Imprime n2

#Solucion 5
if n1<n2: #Condicion si n1 es menor que n2
    print(n2) #Imprime n2
if n2 < n1: #Condicion si n2 es menor que n1
    print(n1) #Imprime n1
if n1==n2: #Condicion si n1 es igual a n2
    print(None) #Imprime None

#Solucion 6
if n1>n2: #Condicion si n1 es mayor que n2
    print(n1) #Imprime n1
if n2>n1: #Condicion si n2 es mayor que n1
    print(n2) #Imprime n2
else: #Si las condiciones no se cumplen ejecuta esta
    print(None) #Imprime None

#Solucion 7
if (n2<n1 or n1>n2): #Condicion con or si se cumple una o la otra
    print(n1) #Imprime n1
elif (n1<n2 or n2>n1): #Condicion con or
    print(n2) #Imprime n2
else: #Si no se cumplen las condiciones anteriores
    print (None) #Imprime None

#Solucion 8
if n1<=n2: #Condicion si n1 es mayor o igual a n2
    if n2 == n1: #If anidados si n2 es igual a n1
        print(None) #Imprime None
    else: #Si no se cumple la sentencia anterior
        print(n2) #Imprime n2
else: #De lo contrario a la sentencia
    print(n1) #Imprime n1

#Solucion 9
if n1 > n2: #Condicion si n1 es mayor que n2
    print(n1) #Imprime n1
elif n2 >= n1: #Condicion si n2 es mayor o igual a n1
    if n2 == n1: #Condicion si n2 es igual a n1
        print(None) #Si es asi imprime None
else: #De lo contrario a las condiciones anteriores
    print(n2) #Imprime n2

#Solucion 10
if n1==n2: #Condicion si n1 es igual a n2
    print (None) #Imprime None
elif n1 < n2: #Condicion si n1 es menor que n2
    print(n2) #Imprime n2
else: #Si no se cumplen alguna condicion anterior se ejecuta esta
    print(n1) #Imprime n1
    
#Solucion 11
if n1 <= n2 and n2==n1: #Condicion con and
    print (None) #Imprime Nnone
elif n1 < n2: #Condicion si n1 es menor que n2
    print (n2) #Imprime n2
else: #Si no se cumplen las condiciones anteriores se ejecuta esta
    print (n1) #Imprime n1
