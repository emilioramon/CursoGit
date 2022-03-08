import collections
import pprint

nombre_archivo = 'pp.txt'

#Hola esto es un nuevo comentario en la rama master con otra rama abierta
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

