class Persona: #Se crea la clase Persona

    __nombre = None
    __email = None

    def  __init__  (self): #Inicializa todo lo que esta dentro de esta linea cuando la llaman
        print ("Persona") #Imprime un mensaje en consola

    def setNombre(self,nombre): #Permite modificar
        self.__nombre = nombre

    def getNombre(self): #Permite mostrar el valor
        return self.__nombre

    def setEmail(self,email): #Permite modificar
        self.__email = email
    
    def getEmail (self): #Permite mostrar el valor
        return self.__email

dejah = Persona () # Llama a la clase persona
dejah.setNombre("Dejah")
dejah.setEmail("dejah126@gmail.com")
print (dejah.getNombre()) # None
print (dejah.getEmail())
# print (dejah.__nombre) se hace privado

john = Persona ()
john.setNombre("John")
john.setEmail("1876512186@utectulancingo.edu.mx")
print (john.getNombre()) # None
print (john.getEmail())

carthoris = Persona ()
carthoris.setNombre("Carthoris")
carthoris.setEmail("1234567899@utectulancingo.edu.mx")
print (carthoris.getNombre()) # None
print (carthoris.getEmail())


aldo = Persona ()
aldo.setNombre("Aldo")
aldo.setEmail("1722110193@utectulancingo.edu.mx")
print (aldo.getNombre()) # None
print (aldo.getEmail())
