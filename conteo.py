import collections
import pprint

nombre_archivo = 'pp.txt'

#Comentario
#Comentario 2
<<<<<<< HEAD
<<<<<<< HEAD
#Rama main
=======
#Comentario branch
=======
>>>>>>> 587e85831aad05cfedff2f5617b252aae1b0301d

>>>>>>> Rama1

with open(nombre_archivo,'r') as f:
    conteo_caracteres = collections.Counter(f.read().upper())
    salida = pprint.pformat(conteo_caracteres)

#print(conteo_caracteres)


print(salida)

