import tkinter
import pymysql

from tkinter import *
from tkinter import messagebox
from functions.conexion import *
from bibliotecario import InterfazBibliotecario
from tkinter import ttk
from UserInterface import userInterface

def main_menu():

    global screen
    global icon
    global c_negro
    c_negro = '#010101'

    screen = Tk()
    screen.geometry("300x350")
    screen.title("Inicio de Sesión")
    screen.config(bg=c_negro)
    screen.iconbitmap('./images/icon.ico')

    img = PhotoImage(file='./images/logo.png')
    Label(text='', bg=c_negro).pack()
    lbl_img = tkinter.Label(screen, image= img, width=50, height=50)
    lbl_img.pack()

    Label(text="Acceso al sistema", background=c_negro, fg="#f58929", width="300", height="3", font=("Calibri",15)).pack()
    Label(text="", background=c_negro).pack()

    Button(text="Iniciar Sesión", height="3", width="30",command=login).pack()
    Label(text="", background=c_negro).pack()
    Button(text="Registrar", height="3", width="30",command=register).pack()

    screen.mainloop()

def login():

    global screen1

    screen1 = Toplevel(screen)
    screen1.geometry("300x350")
    screen1.title("Inicio de sesión")
    screen1.iconbitmap('./images/icon.ico')
    screen1.config(bg= c_negro)

    Label(screen1, text="Ingrese su rut y contraseña",background=c_negro ,fg="#f58929", width="300", height="3", font=("Calibri",15)).pack()
    Label(screen1, text="" , bg=c_negro)

    global l_rut_verify
    global l_pass_verify

    l_rut_verify = StringVar()
    l_pass_verify = StringVar()

    global l_rut_entry
    global l_pass_entry

    Label(screen1, text="RUT", background=c_negro ,fg="white").pack()
    l_rut_entry = Entry(screen1, textvariable= l_rut_verify)
    l_rut_entry.pack()
    Label(screen1, background=c_negro).pack()


    Label(screen1, text="Contraseña", background=c_negro ,fg="white").pack() 
    l_pass_entry = Entry(screen1, textvariable= l_pass_verify, show='*')
    l_pass_entry.pack()
    Label(screen1, background=c_negro).pack()

    Button(screen1, text="Iniciar sesión", command=validate_data).pack()

def register():

    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("300x550")
    screen3.title("Registro")
    screen3.iconbitmap('./images/icon.ico')
    screen3.config(background=c_negro)

    global r_rut_entry
    global r_name_entry
    global r_pass_entry
    global r_adress_entry
    global r_lastname_entry
    global r_mail_entry
    global r_phone_entry
    global r_sexo_entry
    global combo

    r_rut_entry = StringVar()
    r_name_entry = StringVar()
    r_pass_entry = StringVar()
    r_lastname_entry = StringVar()
    r_mail_entry = StringVar()
    r_adress_entry = StringVar()
    r_sexo_entry = StringVar()

    Label(screen3, text="Ingrese datos para su registro",background=c_negro ,fg="#f58929", width="300", height="3", font=("Calibri",15)).pack()

    Label(screen3, text="RUT", background=c_negro, fg='white').pack()
    r_rut_entry = Entry(screen3)
    r_rut_entry.pack()

    Label(screen3, text="Nombre", background=c_negro, fg='white').pack()
    r_name_entry = Entry(screen3)
    r_name_entry.pack()

    Label(screen3, text="Apellido", background=c_negro, fg='white').pack()
    r_lastname_entry = Entry(screen3)
    r_lastname_entry.pack()

    Label(screen3, text="Telefono", background=c_negro, fg='white').pack()
    r_phone_entry = Entry(screen3)
    r_phone_entry.pack()

    Label(screen3, text="Correo", background=c_negro, fg='white').pack()
    r_mail_entry = Entry(screen3)
    r_mail_entry.pack()

    Label(screen3, text="Dirección", background=c_negro, fg='white').pack()
    r_adress_entry = Entry(screen3)
    r_adress_entry.pack()

    Label(screen3, text="Contraseña", background=c_negro, fg='white').pack()
    r_pass_entry = Entry(screen3, show='*')
    r_pass_entry.pack()

    Label(screen3, text='Sexo', background=c_negro, fg='white').pack()
    r_sexo_entry = ttk.Combobox(screen3)
    r_sexo_entry['values']=(
        'Masculino',
        'Femenino'
    )
    r_sexo_entry.pack()
    Label(screen3, background=c_negro).pack()

    Button(screen3, text="Registrarse", command=insert_data).pack()

def insert_data():
    bd = pymysql.connect(
        host="b1yuhymgnump7qdljjoe-mysql.services.clever-cloud.com",
        user="uj6mkddz7d4eaxis",
        passwd="1w7I0nvVdbHlTym1JSEz",
        db="b1yuhymgnump7qdljjoe",
        port=3306
        )

    fcursor = bd.cursor()
    sql = "INSERT INTO usuarios (rut, nombre, apellido, telefono, correo, direccion, sexo, clave) VALUES ('{0}','{1}','{2}',{3},'{4}','{5}','{6}','{7}')".format(
        r_rut_entry.get(), r_name_entry.get(), r_lastname_entry.get(), r_phone_entry.get(), r_mail_entry.get(), r_adress_entry.get(), r_sexo_entry.get(), r_pass_entry.get()
        )
    
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
        screen3.withdraw()
    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

def validate_data():
    bd = pymysql.connect(
        host="b1yuhymgnump7qdljjoe-mysql.services.clever-cloud.com",
        user="uj6mkddz7d4eaxis",
        passwd="1w7I0nvVdbHlTym1JSEz",
        db="b1yuhymgnump7qdljjoe",
        port=3306
        )

    fcursor = bd.cursor()
    fcursor.execute("SELECT clave FROM usuarios WHERE rut='"+l_rut_verify.get()+"' AND clave='"+l_pass_verify.get()+"'")

#   BIBLIOTECARIO
    if l_rut_verify.get()=="15040090-1" and l_pass_verify.get()=="Barroso@76":
        messagebox.showinfo(title="Inicio de sesion correcto", message="RUT y Contraseña correcta\nBibliotecario Identificado")
        screen1.destroy()
        screen.withdraw()
        InterfazBibliotecario()

#   ALUMNO
    elif fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesion correcto", message="Usuario y Contraseña correcta")
        screen1.destroy()
        screen.withdraw()
        userInterface()
    #Intefaz docente

    else:
        messagebox.showinfo(title="Inicio de sesion Incorrecto", message="Usuario y Contraseña incorrecta")
    
    bd.close()

    # login.py

main_menu()