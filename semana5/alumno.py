"""
    Programa 12
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 13/02/2023
    Descripción: Programa que crea la clase Alumno con sus atributos
"""
class Alumno: #Se crea la clase Alumno

    __nombre = None #Creacion de la variable privada 
    __matricula = None #Creacion de otra variable privada
    __carrera = None #Crecion de la variable privada

    def __init__ (self): #Define el inicio de la funcion
        print ("Alumno") #Imprime Alumno

    def setNombre (self, nombre): #Metodo para modificar el valor de la variable 
        self.__nombre = nombre #Asigna el valor de nombre a la variable privada __init__

    def getNombre (self): #Metodo para regresar el valor
        return self.__nombre #Regresa el valor de la variable privada __nombre

    def setMatricula (self, matricula): #Metodo para modificar el valor de la variable 
        self.__matricula = matricula #Asigna el valor de nombre a la variable privada __matricula

    def getMatricula (self): #Metodo para regresar el valor
        return self.__matricula #Regresa el valor de la variable privada __matricula

    def setCarrera (self, carrera): #Metodo para modificar el valor de la variable 
        self.__carrera = carrera #Asigna el valor de nombre a la variable privada __carrera

    def getCarrera (self): #Metodo para regresar el valor
        return self.__carrera #Regresa el valor de la variable privada __matricula

jesus = Alumno() #Creacion del objeto jesus
jesus.setNombre("Jesus") #Asignacion del nombre Jesus al objeto jesus
jesus.setMatricula("1722110193") #Asignacion de la matricula al objeto jesus
jesus.setCarrera("Tecnologias de la Informacion") #Asignacion de la carrera al objeto jesus
print (jesus.getNombre()) #Imprime y regresa la variable __nombre
print (jesus.getMatricula()) #Imprime y regresa la variable __matricula
print (jesus.getCarrera())  #Imprime y regresa la variable __carrera