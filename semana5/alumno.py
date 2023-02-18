class Alumno:

    __nombre = None
    __matricula = None
    __carrera = None

    def __init__ (self):
        print ("Alumno")

    def setNombre (self, nombre):
        self.__nombre = nombre

    def getNombre (self):
        return self.__nombre

    def setMatricula (self, matricula):
        self.__matricula = matricula

    def getMatricula (self):
        return self.__matricula

    def setCarrera (self, carrera):
        self.__carrera = carrera

    def getCarrera (self):
        return self.__carrera

jesus = Alumno()
jesus.setNombre("Jesus")
jesus.setMatricula("1722110193")
jesus.setCarrera("Tecnologias de la Informacion")
print (jesus.getNombre())
print (jesus.getMatricula())
print (jesus.getCarrera())