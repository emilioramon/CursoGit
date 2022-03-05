
import pickle
class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)
    
    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)
class ListaPersonas:
    personas=[]

    def __init__(self):

        listaDePersonas=open("ArchivoExterno","ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del archivo externo".format(len(self.personas)))
        except:
            print("EL archivo está vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnArchivoExterno()
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def guardarPersonasEnArchivoExterno(self):
        listaDePersonas=open("ArchivoExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    def mostrarArchivoExterno(self):
        print("La informacion del archivo externo es la siguiente:")
        for p in self.personas:
            print(p)


miLista=ListaPersonas()
#p=Persona("Jose","Masculino",29)
#miLista.agregarPersonas(p)
#p=Persona("Ana ","Femenino",39)
#miLista.agregarPersonas(p)
#p=Persona("Pedro","Masculino",29)
#miLista.agregarPersonas(p)

#miLista.mostrarPersonas()
miLista.mostrarArchivoExterno()
