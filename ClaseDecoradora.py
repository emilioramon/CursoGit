class Decorador(object):
    def __init__(self,funcion):
        super().__init__()
        self.funcion = funcion
    def __call__(self, *args, **kwargs):
        print("Funcion ejecutada ", self.funcion.__name__)
        self.funcion(*args,**kwargs)

@Decorador
def resta(n,m):
    print (n-m)

resta(3,5)