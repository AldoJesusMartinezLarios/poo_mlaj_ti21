"""
    Programa 13
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 13/02/2023
    Descripción: Programa que crea la clase Persona con sus atributos y creación de otras clases
"""
class Persona: #Crecion de la clase Persona
    __nombre = None #Creacion de la variable privada
    __edad = None #Creacion de la variable privada
    
    def __init__ (self): #Constructor de la clase Persona
        print("Persona") #Imprime Persona

    def setNombre(self,nombre): ##Metodo para modificar el valor de la variable 
	    self.__nombre = nombre #Asigna el valor de nombre a la variable privada __nombre
    
class Alumno (Persona): #Crecion de la clase Alumno en Persona
    __matricula = None #Creacion de la variable privada
    
    def __init__ (self): #Constructor de la clase Alumno
        super().__init__()#Llama al consstructor de la clase Persona
        print("Alumno") #Imprime Alumno

objeto_persona = Persona() #Crea el objeto persona
objeto_alumno = Alumno() #Crea el objeto alumno

print(dir(objeto_persona)) #Imprime el directorio del objeto_persona
print(dir(objeto_alumno)) #Imprime el directorio del objeto_alumno