import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from clientes import *
from catalogo import *
from prestamo2 import PrestamosApp
from catalogoUser import *

def userInterface():
    global c_negro
    c_negro = '#010101'

    try:
        base = Tk()
        base.geometry('300x390')
        base.title("Interfaz Usuario")
        base.config(bg=c_negro)
        base.iconbitmap('./images/icon.ico')

        Label(base, text="Usuario", background=c_negro, fg="#f58929", width="300", height="3", font=("Calibri", 15)).pack()

        Button(base, text='Catalogo', height="3", width="30", command=abrir_catalogo_app).pack()
        Label(base, text="", background=c_negro).pack()
        Button(base, text='Prestamo', height="3", width="30", command=abrir_prestamos_app).pack()

        base.mainloop()

    except ValueError as error:
        print(f'Error de interfaz: {error}')

def abrir_prestamos_app():
    nueva_ventana = Toplevel()
    PrestamosApp(nueva_ventana)
def abrir_catalogo_app():
    Catalogo()

if __name__ == "__main__":
    userInterface()
