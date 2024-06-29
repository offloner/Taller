import tkinter as tk

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from clientes import *
from catalogo import *

def userInterface():

    try:
        base = Tk()
        base.geometry('300x350')
        base.title("Interfaz Usuario")

        Label(base, text="Usuario", fg="black", width="300", height="3", font=("Calibri",15)).pack()

        Button(base, text='Historial Solicitudes',height="3", width="30").pack()
        Label(base,text="").pack()
        Button(base, text='Solicitar Prestamo',height="3", width="30").pack()
        Label(base,text="").pack()
        Button(base, text='Solicitar Prorroga',height="3", width="30").pack()

        base.mainloop()

    except ValueError as error:
        print(f'error de interdaz: {error}')



