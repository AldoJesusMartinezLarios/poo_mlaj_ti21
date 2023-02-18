class Persona:
    __nombre = None
    __edad = None
    
    def __init__ (self):
        print("Persona")

    def setNombre(self,nombre):
        self.__nombre = nombre

    def getNombre (self):
        return self.__nombre

    def setEdad(self,edad):
	    self.__edad = edad
    
    def getEdad (self):
        return self.__edad

class Alumno (Persona):
    __nombre = None
    __matricula = None
    
    def __init__ (self):
        super().__init__()
        print("Alumno")

    def setNombre(self,nombre):
	    self.__nombre = nombre

    def getNombre (self):
        return self.__nombre

    def setMatricula(self,matricula):
	    self.__matricula = matricula

    def getMatricula (self):
        return self.__matricula


class Profesor (Persona):
    __no_nomina = None

    def __init__ (self):
        super().__init__()
        print("Profesor")

    def setNoNomina(self,no_nomina):
	    self.__no_nomina = no_nomina

    def getNoNomina (self):
        return self.__no_nomina


class Coordinador (Persona):

    __no_nomina = None
    __carrera_a_cargo = None

    def __init__ (self):
        super().__init__()
        print("Coordinador")

    def setNoNomina(self,no_nomina):
	    self.__no_nomina = no_nomina

    def getNoNomina (self):
        return self.__no_nomina

    def setCarreraaCargo(self,carrera_a_cargo):
	    self.__carrera_a_cargo = carrera_a_cargo

    def getCarreraaCargo (self):
        return self.__carrera_a_cargo

objeto_persona = Persona()
objeto_alumno = Alumno()
objeto_profesor = Profesor()
objeto_coordinador = Coordinador()

print(dir(objeto_persona))
print(dir(objeto_alumno))
print(dir(objeto_profesor))
print(dir(objeto_coordinador))