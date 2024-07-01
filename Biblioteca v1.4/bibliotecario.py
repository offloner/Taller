import tkinter as tk
import tkinter

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from clientes import *
from catalogo import *
from prestamo import *

def InterfazBibliotecario():

    global c_negro
    c_negro = '#010101'

    try:
        base = Tk()
        base.geometry('300x390')
        base.title("Interfaz Bibliotecario")
        base.config(bg=c_negro)
        base.iconbitmap('./images/icon.ico')

        Label(base, text="Bibliotecario", background=c_negro, fg="#f58929", width="300", height="3", font=("Calibri",15)).pack()

        Button(base, text='Catalogo',height="3", width="30", command=Catalogo).pack()
        Label(base,text="", background=c_negro).pack()
        Button(base, text='Clientes',height="3", width="30", command=Formulario).pack()
        Label(base,text="", background=c_negro).pack()
        Button(base, text='Prestamo',height="3", width="30", command=abrir_prestamos_app).pack()

        base.mainloop()

    except ValueError as error:
        print(f'error de interdaz: {error}')
def abrir_prestamos_app():
    nueva_ventana = Toplevel()
    PrestamosApp(nueva_ventana)