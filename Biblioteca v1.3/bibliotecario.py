import tkinter as tk

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from clientes import *
from catalogo import *




def InterfazBibliotecario():

    try:
        base = Tk()
        base.geometry('300x350')
        base.title("Interfaz Bibliotecario")

        Label(base, text="Bibliotecario", fg="black", width="300", height="3", font=("Calibri",15)).pack()

        Button(base, text='Catalogo',height="3", width="30", command=Catalogo).pack()
        Label(base,text="").pack()
        Button(base, text='Clientes',height="3", width="30", command=Formulario).pack()
        Label(base,text="").pack()
        Button(base, text='Prestamo',height="3", width="30").pack()

        base.mainloop()

    except ValueError as error:
        print(f'error de interdaz: {error}')




