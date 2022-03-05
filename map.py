import functools

#Funcion a utilizar con map() y reduce()
def suma(m,n):
    return n+m

#Funcion a utilizar con filter()
def filtrar(n):
    return(n == 'o')

li = [1, -2, 1, -4]
lo = [5,3,6,7]
s ="Hoola Mundo"
x = map(suma,li,lo)
print (x)
y = filter(filtrar,s)
print (y)
print (functools.reduce(suma,lo))

