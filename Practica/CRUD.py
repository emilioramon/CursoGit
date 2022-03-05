from tkinter import *
from tkinter import messagebox
from xml.dom import minicompat
#from funciones import *
from claseConexion import *



raiz=Tk()
raiz.title("ABM DB")
#raiz.resizable(False,False)
#raiz.geometry("450x450")
miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
miPassword=StringVar()
conex=conexionDB("192.168.0.116","3306","eramon","Eramon578#")

#------------------Funciones---------------------------------------------------

def conectar():
    pass
    
def infoAdicional():
    messagebox.showinfo("ADM prueba", "Ejercicio Practico")

def salirApp():
    valor=messagebox.askquestion("Salir","desea salir de la aplicacion?")
    if valor=="yes":
        raiz.destroy()

def limpiarCampos():
    miApellido.set("")
    miDireccion.set("")
    miNombre.set("")
    miId.set("")
    miPassword.set("")
    campo_Comentario.delete(1.0,END)
    

def crearRegistro():
        conex.crear(miNombre.get(),miApellido.get(),miPassword.get(),miDireccion.get(),campo_Comentario.get("1.0",END))

def leerRegistro():
    resultado= conex.leer(miId.get())
    miId.set(resultado[0])
    miNombre.set(resultado[1])
    miPassword.set(resultado[2])
    miApellido.set(resultado[3])
    miDireccion.set(resultado[4])
    campo_Comentario.delete(1.0,END)
    campo_Comentario.insert (1.0, resultado[5])

def actualizarRegisto():
    conex.actualizar(miId.get(),miNombre.get(),miPassword.get(),miApellido.get(),miDireccion.get(),campo_Comentario.get("1.0",END))

def borrarRegistro():
    conex.borrar(miId.get())
   
   



barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)

#-------------------Menu--------------------------------------
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir", command=salirApp)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crearRegistro)
crudMenu.add_command(label="Leer", command=leerRegistro)
crudMenu.add_command(label="Actualizar", command=actualizarRegisto)
crudMenu.add_command(label="Borrar",command=borrarRegistro)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...",command=infoAdicional)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

miFrame=Frame(raiz,width="350", height="450")
miFrame.pack()
minombre=StringVar()

#----------------------Campos-------------------------------------
campo_id=Entry(miFrame, textvariable=miId)
campo_id.grid(row=0,column=1)
label_id=Label(miFrame,text="Id:")
label_id.grid(row=0,column=0, sticky="e", padx=10,pady=10)

campo_Nombre=Entry(miFrame, textvariable=miNombre)
campo_Nombre.grid(row=1,column=1)
campo_Nombre.config(fg="red", justify="right")
label_Nombre=Label(miFrame,text="Nombre:")
label_Nombre.grid(row=1,column=0, sticky="e", padx=10,pady=10)

campo_Password=Entry(miFrame,textvariable=miPassword)
campo_Password.grid(row=2,column=1)
campo_Password.config(show="*")
label_Password=Label(miFrame,text="Password:")
label_Password.grid(row=2,column=0, sticky="e", padx=10,pady=10)

campo_Apellido=Entry(miFrame, textvariable=miApellido)
campo_Apellido.grid(row=3,column=1)
label_Apellido=Label(miFrame,text="Apellido:")
label_Apellido.grid(row=3,column=0, sticky="e", padx=10,pady=10)

campo_Direccion=Entry(miFrame,textvariable=miDireccion)
campo_Direccion.grid(row=4,column=1)
label_Direccion=Label(miFrame,text="Direccion:")
label_Direccion.grid(row=4,column=0,sticky="e", padx=10,pady=10)

campo_Comentario=Text(miFrame, width=16, height=5)
campo_Comentario.grid(row=5,column=1, sticky="e", padx=10,pady=10)
label_Comentario=Label(miFrame,text="Comentario:")
label_Comentario.grid(row=5,column=0)
scrollVert=Scrollbar(miFrame, command=campo_Comentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
campo_Comentario.config(yscrollcommand=scrollVert.set)


#--------------------Botones-------------------------------------
miFrame2=Frame(raiz)
miFrame2.pack()

botonC=Button(miFrame2,text="Create", command=crearRegistro)
botonC.grid(row=1, column=0, sticky="e", padx=2, pady=5)
botonR=Button(miFrame2,text="Read", command=leerRegistro)
botonR.grid(row=1, column=1, sticky="e",padx=2,pady=5)
botonU=Button(miFrame2,text="Update", command=actualizarRegisto)
botonU.grid(row=1, column=2, sticky="e",padx=2,pady=5)
botonD=Button(miFrame2,text="Delete", command=borrarRegistro)
botonD.grid(row=1, column=3, sticky="e",padx=2,pady=5)

raiz.mainloop()
