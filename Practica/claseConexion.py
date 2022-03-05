from asyncio.windows_events import NULL
from distutils.util import Mixin2to3
import mimetypes
from msilib.schema import SelfReg
from tkinter import messagebox
from typing_extensions import Self
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import mysql.connector


class conexionDB():

    def __init__(self,ho,po,usr,pas) -> None:    
 
            try:
                 self.__mydb = mysql.connector.connect(
                        host=ho,
                        port=po,
                        user=usr,
                        password=pas
                    )
            except:
                   print("Chequee que la base este levantada")
                   return "Error de conexion"
    
            self.__miCursor=self.__mydb.cursor()

            try:
                self.__miCursor.execute("create database miBase")
                self.__miCursor.execute("use miBase")
                self.__miCursor.execute('''
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
                   self.__miCursor.execute("use miBase")
                   messagebox.showwarning("Atencion!", "La BBDD ya exite")
        
    def crear(self,nom, ape, psswd, dire, comen):
            
          self.__miCursor.execute("use miBase")
        
          try:
               self.__miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + nom +
                 "','" + psswd +
                 "','" + ape +
                 "','" + dire +
                 "','" + comen + "')")          
               self.__miCursor.execute("commit;")
               messagebox.showinfo("DB", "Registro incertado con éxito")
          except:
                 messagebox.showwarning("Error","No se pudo incertar")
    
    def leer(self,id):
    
          self.__miCursor.execute("use miBase")
          self.__miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID_USUARIO=" + id)
          query=self.__miCursor.fetchall()
          resultado=[]
          for rr in query:
               resultado.append(rr[0])
               resultado.append(rr[1])
               resultado.append(rr[2])
               resultado.append(rr[3])
               resultado.append(rr[4])
               resultado.append(rr[5])
          return resultado 

    def actualizar(self,id, nombre, passwd, apellido, direccion, comentario):
    
        self._miCursor.execute("use miBase")
        self.__miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+ nombre +
            "', PASSWORD='" + passwd +
            "', APELLIDO='" + apellido +
            "', DIRECCION='" + direccion +
            "', COMENTARIOS='" + comentario +
            "' WHERE ID_USUARIO= " + id) 

        self.__mydb.commit()
        messagebox.showinfo("DB", "Registro actualizado con exito")

    def borrar(self,id):
        self.__miCursor.execute("use miBase")
        self.__miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID_USUARIO=" + id)
        self.__mydb.commit()
        messagebox.showinfo("DB","Se ha borrado el registro con exito")  

       
    


