import collections
import pprint

nombre_archivo = 'pp.txt'

#Comentario
#Comentario 2
#Rama main
#Comentario branch
# Rama1
#Otro comentario en el main

with open(nombre_archivo,'r') as f:
    conteo_caracteres = collections.Counter(f.read().upper())
    salida = pprint.pformat(conteo_caracteres)

#print(conteo_caracteres)


print(salida)

