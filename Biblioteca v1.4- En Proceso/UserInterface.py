import tkinter as tk
import tkinter

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from clientes import *
from catalogo import *
from prestamo import InterfazPrestamo


def userInterface():

    global c_negro
    c_negro = '#010101'

    try:
        base = Tk()
        base.geometry('300x390')
        base.title("Interfaz Usuario")
        base.config(bg=c_negro)
        base.iconbitmap('./images/icon.ico')


        Label(base, text="Usuario", background=c_negro , fg="#f58929", width="300", height="3", font=("Calibri",15)).pack()

        Button(base, text='Historial Solicitudes',height="3", width="30").pack()
        Label(base,text="", background=c_negro).pack()
        Button(base, text='Solicitar Prestamo',height="3", width="30", command=InterfazPrestamo).pack()
        Label(base,text="", background=c_negro).pack()
        Button(base, text='Solicitar Prorroga',height="3", width="30").pack()

        Label(base,text="", background=c_negro).pack()
        Label(base,text="", background=c_negro).pack()

        Button(base, text='Cerrar Sesión').pack()

        base.mainloop()

    except ValueError as error:
        print(f'Error de interfaz: {error}')

