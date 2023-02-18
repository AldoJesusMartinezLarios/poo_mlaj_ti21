class Persona: #Creacion de la clase Persona
    __nombre = None #Creacion de la variable privada
    __edad = None #Crecion de la variable privada
    
    def __init__ (self):  #Inicializa todo lo que esta dentro de esta linea cuando la llaman
        print("Persona") #Imprime Persona

    def setNombre(self,nombre): #Metodo para modificar el valor de la variable
        self.__nombre = nombre  #Asigna el valor de nombre a la variable privada __nombre

    def getNombre (self): #Metodo para mostrar el valor
        return self.__nombre #Regresa el valor de la variable __nombre

    def setEdad(self,edad): #Metodo para modificar el valor de la variable
	    self.__edad = edad #Asigna el valor de nombre a la variable privada __edad
    
    def getEdad (self): #Metodo para mostrar el valor
        return self.__edad #Regresa el valor de la variable __edad

class Alumno (Persona): #Creacion de la clase Alumno en Persona
    __nombre = None #Creacion de la variable __nombre
    __matricula = None #Creacion de la variable __matricula
    
    def __init__ (self): #Inicializa todo lo que esta dentro de esta linea cuando la llaman
        super().__init__() #Llama al consstructor de la clase Persona
        print("Alumno") #Imprime Alumno

    def setNombre(self,nombre): #Metodo para modificar el valor de la variable
	    self.__nombre = nombre #Modifica el valor de la variable

    def getNombre (self): #Metodo para mostrar el valor
        return self.__nombre #Regresa el valor de la variable __nombre

    def setMatricula(self,matricula): #Metodo para modificar el valor de la variable
	    self.__matricula = matricula #Modifca el valor de la variable

    def getMatricula (self): #Metodo para mostrar el valor
        return self.__matricula #Regresa el valor de la variable __matricula


class Profesor (Persona): #Creacion de la clase Profesor en Persona
    __no_nomina = None #Creacion de la variable privada

    def __init__ (self): #Inicializa todo lo que esta dentro de esta linea cuando la llaman
        super().__init__() #Llama al constructor de la clase Persona
        print("Profesor") #Imprime Profesor

    def setNoNomina(self,no_nomina): #Metodo para modificar el valor de la variable
	    self.__no_nomina = no_nomina #Asigna el valor de nombre a la variable privada __no_nomina

    def getNoNomina (self): #Metodo para mostrar el valor
        return self.__no_nomina #Regresa el valor de la variable __no_nomina


class Coordinador (Persona): #Creacion de la clase Coordinador en Persona

    __no_nomina = None #Creacion de la variable privada
    __carrera_a_cargo = None #Creacion de la variable privada

    def __init__ (self): #Inicializa todo lo que esta dentro de esta linea cuando la llaman
        super().__init__() #Llama al constructor de la clase Persona
        print("Coordinador") #Imprime Coordinador

    def setNoNomina(self,no_nomina):  #Metodo para modificar el valor de la variable
	    self.__no_nomina = no_nomina #Asigna el valor de nombre a la variable privada __no_nomina

    def getNoNomina (self): #Metodo para mostrar el valor
        return self.__no_nomina #Regresa el valor de la variable __no_nomina

    def setCarreraaCargo(self,carrera_a_cargo): #Metodo para modificar el valor de la variable
	    self.__carrera_a_cargo = carrera_a_cargo #Asigna el valor de nombre a la variable privada __carrera_a_cargo

    def getCarreraaCargo (self): #Metodo para mostrar el valor
        return self.__carrera_a_cargo #Regresa el valor de la variable __carrera_a_cargo

objeto_persona = Persona() #Se crea el objeto Persona
objeto_alumno = Alumno() #Se crea el objeto alumno
objeto_profesor = Profesor() #Se crea el objeto profesor
objeto_coordinador = Coordinador() #Se crea el objeto coordinador

print(dir(objeto_persona)) #Imprime el directorio del objeto persona
print(dir(objeto_alumno)) #Imprime el directorio del objeto alumno
print(dir(objeto_profesor)) #Imprime el directorio del objeto profesor
print(dir(objeto_coordinador)) #Imprime el directorio del objeto coordinador