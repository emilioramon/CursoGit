import mysql.connector


mydb = mysql.connector.connect(
             host="192.168.0.116",
             port="3306",
             user="eramon",
             password="Eramon578#"
             )

miCursor=mydb.cursor()

try:
    miCursor.execute("use miBase")
except:
       miCursor.execute("create database miBase")
       miCursor.execute("use miBase")

miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID_USUARIO INTEGER PRIMARY KEY AUTO_INCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')