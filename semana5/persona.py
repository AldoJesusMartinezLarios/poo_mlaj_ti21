class Persona: #Se crea la clase Persona

    __nombre = None #Crecion de la variable privada
    __email = None #Creacion de la variable privada

    def  __init__  (self): #Inicializa todo lo que esta dentro de esta linea cuando la llaman
        print ("Persona") #Imprime un mensaje en consola

    def setNombre(self,nombre): #Permite modificar
        self.__nombre = nombre #Asigna el valor de nombre a la variable privada __nombre

    def getNombre(self): #Permite mostrar el valor
        return self.__nombre #Regresa el valor de la variable

    def setEmail(self,email): #Permite modificar
        self.__email = email #Asigna el valor de nombre a la variable privada __email
    
    def getEmail (self): #Permite mostrar el valor
        return self.__email #Regresa el valor de la variable

dejah = Persona () # Llama a la clase persona
dejah.setNombre("Dejah") #Modifica el nombre 
dejah.setEmail("dejah126@gmail.com") #Modifica el valor de email
print (dejah.getNombre()) # Immprime el nombre
print (dejah.getEmail()) #Imprime el email
# print (dejah.__nombre) se hace privado

john = Persona () #Crea un objeto en la clase Persona
john.setNombre("John") #Modifica el valor de nombre
john.setEmail("1876512186@utectulancingo.edu.mx") #odifica el valor de email
print (john.getNombre()) #Imprime el valor de nombre
print (john.getEmail()) #Imprime el valor de email

carthoris = Persona () #Crea un objeto en la clase Persona
carthoris.setNombre("Carthoris") #Asigna valor a la variable nombre
carthoris.setEmail("1234567899@utectulancingo.edu.mx") #Asigna valor a la variable email
print (carthoris.getNombre()) # Imprime el nombre
print (carthoris.getEmail()) #Imprime el email 


aldo = Persona () #Se crea un objeto de la clase Persona
aldo.setNombre("Aldo") #Se le asigna un valor a la nombre
aldo.setEmail("1722110193@utectulancingo.edu.mx") #Se le asigna un valor a la variable email
print (aldo.getNombre()) #Imprime el nombre
print (aldo.getEmail()) #Imprime el email
