import mysql.connector

mydb = mysql.connector.connect(
           host="192.168.0.116",
           port="3306",
           user="eramon",
           password="Eramon578#"
           )

miCursor=mydb.cursor()
miCursor.execute("use miBase")

miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'Emilio','Hola123','Ramon','Lavalleja','No se');")
miCursor.execute("commit;")



    