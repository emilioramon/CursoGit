import pickle

lista_nombres=["Pedro","Ana","Maria","Isabel"]

#Escritura binaria
archivo_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres, archivo_binario)

archivo_binario.close()

#Borrar el archivo de la memoria
del(archivo_binario)