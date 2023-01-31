"""
    Programa 7
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 31/01/2023
    Descripción: Calculo de perimetro y area de circulo
"""

print ("PROGRAMA QUE CALCULA EL AREA Y EL PERIMETRO DEL CIRCULO") #Imprime un mensaje en consola

pi = 3.1416
radio = float(input("El radio es: ")) #Pide el valor de la variable radio al usuario

perimetro = 2 * pi * radio #Formula para calcular el perimetro
area = pi * radio ** 2 #Formula para calcular el area

print("El area de un circulo de ",radio," de radio es ", area," cm²") #Imprime el resultado
print("El perimetro de un circulo de ",radio," de radio es ", perimetro) #Imprime el resultado

print("PROGRAMA QUE CALCULA EL AREA Y EL PERIMETRO DE UN CUADRADO") #Imprime un mensaje en consola

lado = float(input("Lado del cuadrado: ")) #Pide el valor del lado

perimetro = lado * 4 #Formula para sacar el perimetro de un cuadrado
area = lado * lado #Formula para sacar el area de un cuadrado

print("El area de un cuadrado de ",lado," lado es ", area, "cm²") #Imprime el resultado del area
print("El perimetro de un cuadrado de ",lado," lado es",perimetro, "cm") #Imprime el resultado del perimetro 
