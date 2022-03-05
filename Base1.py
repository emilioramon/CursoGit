from sqlite3 import Cursor
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.116",
  port="3306",
  user="eramon",
  password="Eramon578#"
)

miCursor=mydb.cursor()
miCursor.execute("use basepython;")

variosProductos= [
  ('Pan', 150, 1),
  ('Yerba', 200, 2),
  ('Cafe', 400, 3),
  ('Te', 250, 4)
]


#miCursor.executemany("INSERT INTO Productos  VALUES (?,?,?)", variosProductos)
miCursor.execute("INSERT INTO Productos (codigo,nombre,precio) VALUES (1,'Pan',150)")
miCursor.execute("INSERT INTO Productos (codigo,nombre,precio) VALUES (2,'Yerba',200)")
miCursor.execute("INSERT INTO Productos (codigo,nombre,precio) VALUES (3,'Cafe',400)")
miCursor.execute("INSERT INTO Productos (codigo,nombre,precio) VALUES (4,'Te',250)")
miCursor.execute("INSERT INTO Productos (codigo,nombre,precio) VALUES (5,'Queso',500)")
mydb.commit()

#tabla=miCursor.execute("select * from Productos")
variosProductos=miCursor.fetchall()

for producto in variosProductos:
  print("Producto: ", producto[0], "Precio: ", producto[1], "Codigo: ", producto[2])

mydb.close()