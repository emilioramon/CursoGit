try:
    valor = input("Intruduzca un numero:")
    valor2 = input("Introduzca otro numero:")
    valor = int(valor)
    valor2 = int(valor2)
except:
    print ("No es un numero")
else:
    print ("Suma de %d y %d es : %d" % (valor, valor2, valor+valor2))
    print (type(valor))
