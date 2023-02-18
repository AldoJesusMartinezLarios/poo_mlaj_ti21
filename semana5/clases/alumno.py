"""
    Programa 17
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 16/02/2023
    Descripción: Programa que crea la clase alumno importando la clase Persona
"""
from persona import Persona #Importa del archivo persona.py la clase Persona

class Alumno(Persona): #Crea la clase Alumno y hereda de la clase Persona

    def __init__(self)->None: #Constructor de la clase Alumno
        super().__init__() #Llama al consstructor de la clase Persona
        print("Constructor Alumno") #Muestra el mensaje "Constructor Alumno"

    

objeto_alumno = Alumno() #Crea un objeto de la clase Alumno e invoca al constructor
objeto_alumno.setNombre("Dejah") #Llama al metodo setNombre de la clase Persona y le otorga este nuevo valor
print(objeto_alumno.getNombre()) #Llama al metodo getNombre e imprime el valor que tiene