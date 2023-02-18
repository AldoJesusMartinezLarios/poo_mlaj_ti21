class Persona: #Creacion de la clase Persona

    __nombre = None #Creacion de la variable privada con el valor None

    def __init__(self)-> None: #Constructor de la clase Persona
        print ("Constructor Persona") #Imprime el texto "Constructor Persona"

    def setNombre(self, nombre:str) -> None: #Metodo para modificar el valor de la variable 
        self.__nombre = nombre #Asigna el valor de nombre a la variable privada __init__
    
    def getNombre(self)->str: #Metodo para regresar el valor 
        return self.__nombre #Regresa el valor de la variable privada __nombre