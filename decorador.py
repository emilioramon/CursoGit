import functools


loggeado = True
usuario = "Emilio"

def admin(f):
    def comprobar(*args,**kwargs):
        if loggeado: 
            f(*args,**kwargs)
        else:
            print("No tiene permisos de ejecutar",f.__name__)
    return comprobar

def decorador(funcion):
    def funcionDecorada(*args,**kwargs):
        print ("Funcion ejecutada: ", funcion.__name__)
        funcion(*args,**kwargs)
    return funcionDecorada

@admin
@decorador
def resta(n,m):
    print(n-m)

resta(3,5)

#Decorardor

#decorador(resta)(5,3)
