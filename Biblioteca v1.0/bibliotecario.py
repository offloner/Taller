import tkinter as tk

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from main import *
from catalogo import *



def InterfazBibliotecario():
    try:
        base = Tk()
        base.geometry('900x300')
        base.title("Interfaz Bibliotecario")
        groupBox = LabelFrame(base, text='Interfaz del bibliotecario', padx=5, pady=5, fg="black", width="300", height="3", font=("Calibri",15))
        groupBox.grid(row=0,column=0,padx=10, pady=10)



        Button(groupBox, text='Catalogo', width=20, command=Catalogo).pack()
        Label(text="")
        Button(groupBox, text='Clientes', width=20, command=Formulario).pack()
        Label(text="")
        Button(groupBox, text='Prestamo', width=20).pack()

        base.mainloop()

    except ValueError as error:
        print(f'error de interdaz: {error}')


