class Humano:
    def __init__(self,edad):
        self.edad = edad
        print ('Soy un humano')
    
    def hablar(self,mensaje):
        print(mensaje)

class IngSistemas(Humano):
    def __init__(self,edad):
        super().__init__(self)
        print('Soy Ingeniero')

    def programar(self,lenguaje):
        print ('Voy a programar en ', lenguaje)

class Abogado(Humano):
    def __init__(self, edad, escuela):
        super().__init__(edad)
        print ('Abogado egresado de; ', escuela)

    def estudiarCaso(self,de):
        print ('debo estudiar el caso de ', de)

class Estudioso(Abogado,IngSistemas):
    pass


pedro = Estudioso(25,'UNAM')
pedro.programar('c++')
pedro.hablar('Hola soy de herencia multiple')
pedro.estudiarCaso('Juan')