import tkinter as tk

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from tkcalendar import *


def InterfazPrestamo():
    try:
        base = Tk()
        base.geometry('1200x300')
        base.title('Formulario Prestamo')\
        
        groupBox = LabelFrame(base, text='Asignacion prestamo', padx=5, pady=5)
        groupBox.grid(row=0,column=0,padx=10, pady=10)

        LabelRut = Label(groupBox, text = 'RUT Cliente: ', width=12, font=('arial',12)).grid(row=0,column=0)
        texBoxId = Entry(groupBox)
        texBoxId.grid(row=0,column=1)

        LabelIsbn = Label(groupBox, text = 'ISBN Libro: ', width=12, font=('arial',12)).grid(row=1,column=0)
        texBoxId = Entry(groupBox)
        texBoxId.grid(row=1,column=1)

        LabelDate = Label(groupBox, text = 'Dias de uso: ', width=12, font=('arial',12)).grid(row=2,column=0)
        texBoxId = Entry(groupBox)
        texBoxId.grid(row=2,column=1)        


        Button(groupBox, text='Guardar', width=10).grid(row=4, column=0)
        Button(groupBox, text ="Cerrar", command=base.withdraw).grid(row=4, column=1)
        base.mainloop()


    except ValueError as error:
        print('error de interfaz: '+ error)
InterfazPrestamo()