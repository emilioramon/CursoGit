from io import open

archivo_texto=open("archivo.txt","r")

#frase="Un buen dia para estudia Python \n el Martes"

#archivo_texto.write(frase)
#archivo_texto.close()

#texto=archivo_texto.read()
lista=archivo_texto.readlines()
#print(texto)
print(lista)
archivo_texto.close()



