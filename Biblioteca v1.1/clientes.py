import tkinter as tk

#importar los modulos restantes de tkinter

from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from functions.CRUDpersonas import *
from functions.conexion import *


class FormularioClientes:
 
 global base
 base=None
 
 global textBoxRut
 textBoxRut=None

 global textBoxNombres
 textBoxNombres=None

 global textBoxApellidos
 textBoxApellidos=None

 global textBoxTelefono
 textBoxTelefono=None

 global textBoxCorreo
 textBoxCorreo=None

 global textBoxDireccion
 textBoxDireccion=None

 global combo
 combo=None

 global groupbox
 groupbox=None

 global tree
 tree=None

 
def Formulario():

    global textBoxRut
    global textBoxNombres
    global textBoxApellidos
    global textBoxTelefono
    global textBoxCorreo
    global textBoxDireccion
    global combo
    global base
    global groupbox
    global tree



    try:
        base = Tk()
        base.geometry("1440x720")
        base.title("Formulario Python")


        groupbox = LabelFrame(base,text="Datos Clientes", padx=8,pady=8)
        groupbox.grid(row=0,column=0,padx=10,pady=10, sticky="ew", columnspan=3)

        labelRut=Label(groupbox,text="Rut:", width=13, font=("Arial",12)).grid(row=0,column=0)
        textBoxRut=Entry(groupbox)
        textBoxRut.grid(row=0,column=1)

        labelNombres=Label(groupbox,text="Nombre:", width=13, font=("Arial",12)).grid(row=1,column=0)
        textBoxNombres=Entry(groupbox)
        textBoxNombres.grid(row=1,column=1)

        labelApellidos=Label(groupbox,text="Apellido:", width=13, font=("Arial",12)).grid(row=2,column=0)
        textBoxApellidos=Entry(groupbox)
        textBoxApellidos.grid(row=2,column=1)

        labelCorreo=Label(groupbox,text="Telefono:", width=13, font=("Arial",12)).grid(row=3,column=0)
        textBoxTelefono=Entry(groupbox)
        textBoxTelefono.grid(row=3,column=1)

        labelTelefono=Label(groupbox,text="Correo:", width=13, font=("Arial",12)).grid(row=4,column=0)
        textBoxCorreo=Entry(groupbox)
        textBoxCorreo.grid(row=4,column=1)

        labelDireccion=Label(groupbox,text="Direccion:", width=13, font=("Arial",12)).grid(row=5,column=0)
        textBoxDireccion=Entry(groupbox)
        textBoxDireccion.grid(row=5,column=1)

        labelSexo=Label(groupbox,text="Sexo:", width=13, font=("Arial",12)).grid(row=6,column=0)
        seleccionSexo=tk.StringVar()
        combo=ttk.Combobox(groupbox,values=["Masculino", "Femenino", "Otro"], textvariable=seleccionSexo)
        combo.grid(row=6,column=1)
        seleccionSexo.set("Seleccionar")

        Button(groupbox,text="Guardar", width=10, command=guardarRegistros).grid(row=7,column=0)
        Button(groupbox,text="Modificar", width=10, command=modificarRegistros).grid(row=7,column=1)
        Button(groupbox,text="Eliminar", width=10, command=eliminarRegistros).grid(row=7,column=2)
        

        groupbox = LabelFrame(base,text="Lista de Clientes", padx=5,pady=5,)
        groupbox.grid(row=1,column=0,padx=5,pady=5,sticky="ew", columnspan=3)
        #Crear un treeview

        #Configurar las columnas

        tree = ttk.Treeview(groupbox, columns=("Rut","Nombres","Apellidos","Telefono", "Correo", "Direccion", "Sexo"), show='headings', height=7,)

        tree.column("# 1",anchor=CENTER)
        tree.heading("# 1", text="Rut")

        tree.column("# 2",anchor=CENTER)
        tree.heading("# 2", text="Nombres")
        
        tree.column("# 3",anchor=CENTER)
        tree.heading("# 3", text="Apellidos")

        tree.column("# 4",anchor=CENTER)
        tree.heading("# 4", text="Telefono")

        tree.column("# 5",anchor=CENTER)
        tree.heading("# 5", text="Correo")

        tree.column("# 6",anchor=CENTER)
        tree.heading("# 6", text="Direccion")

        tree.column("# 7",anchor=CENTER)
        tree.heading("# 7", text="Sexo")

        #Agregar los datos a la tabla
        #Mostrar la tabla

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

        #Ejecutar la funcion al hacer click y mostrar el resultado en los entry
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

        tree.pack()

        base.mainloop()


    except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))

def guardarRegistros():
    
     global textBoxRut, textBoxNombres, textBoxApellidos, combo, groupbox, textBoxCorreo, textBoxTelefono, textBoxDireccion


     try:
         #verificar si los widgets estan inicializados
         if textBoxRut is None or textBoxNombres is None or textBoxApellidos is None or combo is None or textBoxCorreo is None or textBoxTelefono is None or textBoxDireccion is None:
             print("Los widgets no han sido inicializados")
             return
         rut = textBoxRut.get()
         nombres = textBoxNombres.get()
         apellidos = textBoxApellidos.get()
         telefono = textBoxTelefono.get()
         correo = textBoxCorreo.get()
         direccion = textBoxDireccion.get()
         sexo = combo.get()
         CClientes.ingresarClientes(rut, nombres, apellidos, telefono, correo, direccion, sexo, clave)
         messagebox.showinfo("Informacion", "Registro ingresado correctamente")

         actualizarTreeView()
        
            #limpiamos los campos
         textBoxRut.delete(0,END)
         textBoxNombres.delete(0,END)
         textBoxApellidos.delete(0,END)
         textBoxTelefono.delete(0,END)
         textBoxCorreo.delete(0,END)
         textBoxDireccion.delete(0,END)

     except ValueError as error:
         print("Error al ingresar los datos, error: {}".format(error))

def actualizarTreeView():
    global tree

    try:
        #borrar todos los elementos actuales del treeview a mano
        tree.delete(*tree.get_children())

        #obtener los nuevos datos que deseamos mostrar

        datos = CClientes.mostrarClientes()

        #Insertar los nuevos datos en el treeview

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

    except ValueError as error:
        print("Error al actualizar el treeview, error: {}".format(error))
def seleccionarRegistro(event):
    try:
        itemSeleccionado = tree.focus()

        if itemSeleccionado:
            #obtener los valores por columna
            values = tree.item(itemSeleccionado)["values"]

            #Establecer los valores en los widgets

            textBoxRut.delete(0,END)
            textBoxRut.insert(0,values[0])

            textBoxNombres.delete(0,END)
            textBoxNombres.insert(0,values[1])

            textBoxApellidos.delete(0,END)
            textBoxApellidos.insert(0,values[2])

            textBoxTelefono.delete(0,END)
            textBoxTelefono.insert(0,values[3])

            textBoxCorreo.delete(0,END)
            textBoxCorreo.insert(0,values[4])

            textBoxDireccion.delete(0,END)
            textBoxDireccion.insert(0,values[5])
            combo.set(values[6])

    except ValueError as error:
        print("Error al seleccionar el registro, error: {}".format(error))

def modificarRegistros():
    
     global textBoxRut, textBoxNombres, textBoxApellidos, combo, groupbox, textBoxDireccion, textBoxCorreo, textBoxTelefono


     try:
         #verificar si los widgets estan inicializados
         if textBoxRut is None or textBoxNombres is None or textBoxApellidos is None or combo is None or textBoxTelefono is None or textBoxDireccion is None or textBoxCorreo is None:
             print("Los widgets no han sido inicializados")
             return
         idUsuario = textBoxRut.get()
         nombre = textBoxNombres.get()
         apellido = textBoxApellidos.get()
         sexo = combo.get()
         telefono = textBoxTelefono.get()
         correo = textBoxCorreo.get()
         direccion = textBoxDireccion.get()

         CClientes.modificarClientes(idUsuario, nombre, apellido, telefono, correo, direccion, sexo)
         messagebox.showinfo("Informacion", "Los datos fueron modificados correctamente")

         actualizarTreeView()
        
            #limpiamos los campos
         textBoxRut.delete(0,END)
         textBoxNombres.delete(0,END)
         textBoxApellidos.delete(0,END)
         textBoxDireccion.delete(0,END)
         textBoxTelefono.delete(0,END)
         textBoxCorreo.delete(0,END)

     except ValueError as error:
         print("Error al modificar los datos, error: {}".format(error))

def eliminarRegistros():
    
     global textBoxRut, textBoxNombres, textBoxApellidos


     try:
         #verificar si los widgets estan inicializados
         if textBoxRut is None:
             print("Los widgets no han sido inicializados")
             return
         idUsuario = textBoxRut.get()

         CClientes.eliminarClientes(idUsuario)
         messagebox.showinfo("Informacion", "Los datos fueron eliminados correctamente")

         actualizarTreeView()
        
            #limpiamos los campos
         textBoxRut.delete(0,END)
         textBoxNombres.delete(0,END)
         textBoxApellidos.delete(0,END)
         textBoxDireccion.delete(0,END)
         textBoxTelefono.delete(0,END)
         textBoxCorreo.delete(0,END)
     except ValueError as error:
         print("Error al ingresar los datos, error: {}".format(error))








