import tkinter as tk
#importar los modulos restantes de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from conexion import *
from CRUDcatalogo import *



class CatalogoLibros:

    global groupbox
    groupbox=None

    global textBoxISBN
    textBoxISBN = None

    global textBoxNombre
    textBoxNombre = None

    global textBoxAutor
    textBoxAutor = None

    global textBoxGenero
    textBoxGenero = None

    global textBoxEditorial
    textBoxEditorial = None

    global textBoxAño
    textBoxAño = None

    global interfazCatalogo
    interfazCatalogo = None

    global tree2
    tree2 = None


def Catalogo():

    try:
        interfazCatalogo = Tk()
        interfazCatalogo.geometry("1280x720")
        interfazCatalogo.title("Catalogo de libros")

        groupbox = LabelFrame(interfazCatalogo,text="Ingresar datos", padx=8,pady=8)
        groupbox.grid(row=0,column=0,padx=10,pady=10, sticky="ew", columnspan=3)

        labelISBN=Label(groupbox,text="ISBN:", width=13, font=("Arial",12)).grid(row=0,column=0)
        textBoxISBN=Entry(groupbox)
        textBoxISBN.grid(row=0,column=1)

        labelNombre=Label(groupbox,text="Nombre:", width=13, font=("Arial",12)).grid(row=1,column=0)
        textBoxNombre=Entry(groupbox)
        textBoxNombre.grid(row=1,column=1)
        
        labelAutor=Label(groupbox,text="Autor:", width=13, font=("Arial",12)).grid(row=2,column=0)
        textBoxAutor=Entry(groupbox)
        textBoxAutor.grid(row=2,column=1)

        labelGenero=Label(groupbox,text="Genero:", width=13, font=("Arial",12)).grid(row=3,column=0)
        textBoxGenero=Entry(groupbox)
        textBoxGenero.grid(row=3,column=1)

        labelEditorial=Label(groupbox,text="Editorial:", width=13, font=("Arial",12)).grid(row=4,column=0)
        textBoxEditorial=Entry(groupbox)
        textBoxEditorial.grid(row=4,column=1)

        labelAño=Label(groupbox,text="Año de Publicacion:", width=17, font=("Arial",12)).grid(row=5,column=0)
        textBoxAño=Entry(groupbox)
        textBoxAño.grid(row=5,column=1)

        Button(groupbox,text="Guardar", width=10, command=guardarRegistros).grid(row=6,column=0)
        Button(groupbox,text="Modificar", width=10).grid(row=6,column=1)
        Button(groupbox,text="Eliminar", width=10).grid(row=6,column=2)
        

        catalogo_frame = ttk.LabelFrame(interfazCatalogo, text="Información Personal", padding=(20, 10))
        catalogo_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tree2 = ttk.Treeview(catalogo_frame, columns=("ISBN","Nombre","Autor","Genero", "Editorial", "Año de publicación"), show='headings', height=6)

        tree2.column("# 1",anchor=CENTER)
        tree2.heading("# 1", text="ISBN")

        tree2.column("# 2",anchor=CENTER)
        tree2.heading("# 2", text="Nombre")
        
        tree2.column("# 3",anchor=CENTER)
        tree2.heading("# 3", text="Autor")

        tree2.column("# 4",anchor=CENTER)
        tree2.heading("# 4", text="Genero")

        tree2.column("# 5",anchor=CENTER)
        tree2.heading("# 5", text="Editorial")

        tree2.column("# 6",anchor=CENTER)
        tree2.heading("# 6", text="Año de publicación")
        #agregar datos a la tabla
        #mostrar el catalogo
        for row in CCatalogo.mostrarCatalogo():
            tree2.insert("","end",values=row)
        

        tree2.pack() 
            
        interfazCatalogo.mainloop()

    except ValueError as error:
        print("Error al ingresar los datos, error: {}".format(error))

def guardarRegistros():
    global textBoxISBN, textBoxNombre, textBoxAutor, textBoxEditorial, textBoxGenero, textBoxAño, groupbox


    try:
        #verificar si los widgets estan inicializados
        if textBoxISBN is None or textBoxNombre is None or textBoxAutor is None or textBoxGenero is None or textBoxEditorial is None or textBoxAño is None or groupbox is None:
            print("Los widgets no estan inicializados")
            return
        ISBN = textBoxISBN.get()
        nombre = textBoxNombre.get()
        autor = textBoxAutor.get()
        genero = textBoxGenero.get()
        editorial = textBoxEditorial.get()
        año = textBoxAño.get()

        CCatalogo.ingresarLibros(ISBN, nombre, autor, genero, editorial, año)
        messagebox.showinfo("Informacion", "Los datos fueron guardados")

        #Limpiamos los campos

        textBoxISBN.delete(0,END)
        textBoxNombre.delete(0,END)
        textBoxAutor.delete(0,END)
        textBoxGenero.delete(0,END)
        textBoxEditorial.delete(0,END)
        textBoxAño.delete(0,END)

    except ValueError as error:
        print("Error al ingresar los datos, error: {}".format(error))

