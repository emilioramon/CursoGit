from distutils.util import Mixin2to3
import mimetypes
from tkinter import messagebox
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import mysql.connector

def conectar():
    try:
         mydb = mysql.connector.connect(
             host="192.168.0.116",
             port="3306",
             user="eramon",
             password="Eramon578#"
             )
    except:
        print("Chequee que la base este conectada")
        return "Error de conexion"
    
    miCursor=mydb.cursor()

    try:
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

        messagebox.showinfo("Base Creada", "La base se creo con exito")

    except:
           miCursor.execute("use miBase")
           messagebox.showwarning("Atencion!", "La BBDD ya exite")

def crearCursor():
    mydb = mysql.connector.connect(
              host="192.168.0.116",
              port="3306",
              user="eramon",
              password="Eramon578#"
              )
    return mydb.cursor()

def crear(nom, ape, psswd, dire, comen):
    
    mydb = mysql.connector.connect(
              host="192.168.0.116",
              port="3306",

              user="eramon",
              password="Eramon578#"
              )
    miCursor=mydb.cursor()
    miCursor.execute("use miBase")
    try:
        miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + nom +
            "','" + psswd +
            "','" + ape +
            "','" + dire +
            "','" + comen + "')")          
        miCursor.execute("commit;")
        messagebox.showinfo("DB", "Registro incertado con éxito")
    except:
        messagebox.showwarning("Error","No se pudo incertar")
        
def leer(id):
    mydb = mysql.connector.connect(
              host="192.168.0.116",
              port="3306",

              user="eramon",
              password="Eramon578#"
              )
    miCursor=mydb.cursor()
    miCursor.execute("use miBase")
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID_USUARIO=" + id)
    query=miCursor.fetchall()
    resultado=[]
    for rr in query:
        resultado.append(rr[0])
        resultado.append(rr[1])
        resultado.append(rr[2])
        resultado.append(rr[3])
        resultado.append(rr[4])
        resultado.append(rr[5])
    return resultado 

def actualizar(id, nombre, passwd, apellido, direccion, comentario):
    
    mydb = mysql.connector.connect(
              host="192.168.0.116",
              port="3306",
              user="eramon",
              password="Eramon578#"
              )
    miCursor=mydb.cursor()
    miCursor.execute("use miBase")
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+ nombre +
        "', PASSWORD='" + passwd +
        "', APELLIDO='" + apellido +
        "', DIRECCION='" + direccion +
        "', COMENTARIOS='" + comentario +
        "' WHERE ID_USUARIO= " + id) 

    mydb.commit()
    messagebox.showinfo("DB", "Registro actualizado con exito")

def borrar(id):
    mydb = mysql.connector.connect(
              host="192.168.0.116",
              port="3306",
              user="eramon",
              password="Eramon578#"
              )
    miCursor=mydb.cursor()
    miCursor.execute("use miBase")
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID_USUARIO=" + id)
    mydb.commit()
    messagebox.showinfo("DB","Se ha borrado el registro con exito")  

       
    


