class UnoError(Exception):
      def __init__(self,valor):
         self.valorError= valor
      def __str__(self):
         print("No se puede dividir entre 1 el numero: ", self.valorError)

d = 5
n = 1
#try:
if n==1:
     raise UnoError(d)
#except UnoError:
#    print ("Se ha producido un error que yo cree")

